import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import os, sys

def g(tes_amount):
    """Generate vertices of a 4D square (tesseract)."""
    vertices = []
    for i in range(tes_amount):
        for x in [i, i+1]:
            for y in [i, i+1]:
                for z in [i, i+1]:
                    for w in [i, i+1]:
                        vertices.append([x, y, z, w])
    return np.array(vertices)

def g_lines(tes_amount):
    """Generate lines of a 4D square (tesseract)."""
    lines = []
    vertices = []

    for i in range(tes_amount):
        # Generate the vertices first
        for x in [i, i+1]:
            for y in [i, i+1]:
                for z in [i, i+1]:
                    for w in [i, i+1]:
                        vertices.append([x, y, z, w])

        # Generate lines connecting vertices
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                # Check if the vertices are adjacent (Hamming distance of 1)
                if np.sum(np.abs(np.array(vertices[i]) - np.array(vertices[j]))) == 1:
                    lines.append((vertices[i], vertices[j]))

    return np.array(lines)


def rotate_4D(points, angles):
    theta, phi, psi = angles

    # Create rotation matrices
    R_xy = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    R_xz = np.array([
        [np.cos(phi), 0, -np.sin(phi), 0],
        [0, 1, 0, 0],
        [np.sin(phi), 0, np.cos(phi), 0],
        [0, 0, 0, 1]
    ])

    R_xw = np.array([
        [np.cos(psi), 0, 0, -np.sin(psi)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [np.sin(psi), 0, 0, np.cos(psi)]
    ])

    # Combine rotations
    R = R_xy @ R_xz @ R_xw
    rotated_points = np.dot(points, R.T)
    return rotated_points

def project_to_3D(points_4D):
    """Project 4D points onto a toroidal surface in 3D space."""
    x, y, z, w = points_4D[:, 0], points_4D[:, 1], points_4D[:, 2], points_4D[:, 3]
    
    # Example toroidal projection formula
    # Here, we can wrap the z-coordinate to simulate a toroidal effect
    toroidal_radius = 5
    projected_x = (x / (1 + np.abs(w))) * toroidal_radius
    projected_y = (y / (1 + np.abs(w))) * toroidal_radius
    projected_z = (z % (2 * np.pi)) - np.pi  # Wrap around z

    return np.array([projected_x, projected_y, projected_z]).T

def draw_points(points):
    glBegin(GL_POINTS)
    for point in points:
        glVertex3fv(point)
    glEnd()

def pointloop():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -30)

    num_points = 1000
    points_4D = g(50)
    angles = (np.pi / 4, np.pi / 4, np.pi / 4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 0, 1, 0)  # Rotate the scene

        rotated_points = rotate_4D(points_4D, angles)
        projected_points = project_to_3D(rotated_points)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_points(projected_points)

        pygame.display.flip()
        pygame.time.wait(10)

def draw_lines(lines):
    glBegin(GL_LINES)
    for start, end in lines:
        glVertex3fv(start[:3])  # Use only the first three dimensions
        glVertex3fv(end[:3])    # Use only the first three dimensions
    glEnd()

def lineloop():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -30)

    num_points = 1000
    lines_4D = g_lines(5)
    angles = (np.pi / 4, np.pi / 2, np.pi / 8) # spline
    # angles = (np.pi / 2, np.pi / 2, np.pi / 2)

    rotated_lines = [(rotate_4D(np.array([start]), angles)[0], rotate_4D(np.array([end]), angles)[0]) for start, end in lines_4D]
    projected_lines = [(project_to_3D(np.array([start]))[0], project_to_3D(np.array([end]))[0]) for start, end in rotated_lines]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 0, 1, 0)  # Rotate the scene

        # Rotate and project each endpoint of the lines separately
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_lines(projected_lines)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    if '--points' in sys.argv:
        pointloop()
    else:
        lineloop()
    
