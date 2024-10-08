import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def convert_4x6_to_4x4(matrix_4x6):
    """ Convert a 4x6 matrix to a 4x4 matrix by taking the first four columns. """
    return np.array(matrix_4x6[:, :4], dtype=float)

def get_circle_matrix(rotation, translation):
    """ Create a 4x6 matrix representing a circle transformation. """
    cos_r = np.cos(rotation)
    sin_r = np.sin(rotation)
    # Create a 4x6 matrix, the last two columns will be filled with zeros
    matrix = np.zeros((4, 6))
    matrix[0, 0] = cos_r
    matrix[0, 1] = -sin_r
    matrix[0, 4] = translation[0]
    matrix[1, 0] = sin_r
    matrix[1, 1] = cos_r
    matrix[1, 4] = translation[1]
    matrix[2, 2] = 1
    matrix[2, 4] = translation[2]
    matrix[3, 3] = 1
    return matrix

# Create 4x6 matrices for the circles with variance
M1 = get_circle_matrix(0, [0, 0, 0])          # Circle 1 (Center)
M2 = get_circle_matrix(0.2, [0.5, 0.3, 0])    # Circle 2 (Right-Top)
M3 = get_circle_matrix(-0.4, [0.6, -0.4, 0])  # Circle 3 (Right-Bottom)
M4 = get_circle_matrix(0.1, [-0.5, -0.5, 0])  # Circle 4 (Left-Bottom)
M5 = get_circle_matrix(-0.2, [-0.3, 0.7, 0])  # Circle 5 (Left-Top)
M6 = get_circle_matrix(0.3, [0.2, -0.8, 0])   # Circle 6 (Center-Bottom)
M7 = get_circle_matrix(-0.1, [-0.6, 0.2, 0])  # Circle 7 (Center-Top)

# Combine the matrices into a list for drawing
matrices_4x6 = [M1, M2, M3, M4, M5, M6, M7]

def get_tesseract_vertices(size):
    """ Generate the vertices of a 6D tesseract. """
    vertices = []
    for i in range(64):  # 2^6 = 64 vertices
        vertex = [
            size * ((i >> d) & 1) for d in range(6)  # Each dimension can be 0 or size
        ]
        vertices.append(vertex)
    return np.array(vertices)

def project_to_3d(vertex):
    """ Project a 6D vertex to 3D space. """
    proj = []
    for v in vertex:
        proj.append(v*matrices_4x6[0].T*v*matrices_4x6[1].T*v*matrices_4x6[2].T*v*matrices_4x6[3].T*v*matrices_4x6[4].T*v*matrices_4x6[5].T*v*matrices_4x6[6].T)
    scale = 1 / (3 - vertex[3])  # Perspective effect based on the 4th dimension
    return np.array([
        vertex[0] * scale,
        vertex[1] * scale,
        vertex[2] * scale
    ])

def draw_tesseract(vertices):
    """ Draw the tesseract based on its vertices. """
    projected_vertices = [project_to_3d(vertex) for vertex in vertices]
    
    glBegin(GL_LINES)
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if bin(i ^ j).count('1') == 1:  # Connect vertices that differ by one bit
                glVertex3fv(projected_vertices[i])
                glVertex3fv(projected_vertices[j])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)  # Adjusted field of view for zoom
    glTranslatef(0.0, 0.0, -5)  # Closer zoom for better visualization

    vertices = get_tesseract_vertices(3/2)  # Size of the tesseract
    vertices2 = get_tesseract_vertices(1/4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Rotate the tesseract for better visualization
        glRotatef(0.5, 0.5, 0.5, 0.5)
        draw_tesseract(vertices)
        draw_tesseract(vertices2)
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
