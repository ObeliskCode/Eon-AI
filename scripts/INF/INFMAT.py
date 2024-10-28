from infmath import *

def H(informal_set):
    infn = informal_set

    if len(infn) == ((2*max(infn))+1):
        return max(infn)
    return 0


## [WIP] [TODO]
def matrix_2d_add_mult_H(matrix, size):
    # if first row is all 0's matrix is 0
    first_add = False

    sum = 0
    for j in range(size):
        x = matrix[0][j]
        if x == 0:
            continue
        sum += x

    if sum == 0:
        return 0

    compound = 0

    for i in range(size):
        for j in range(size):
            x = matrix[i][j]
            if x < 1:
                continue
            if i == 0:
                if first_add == False:
                    first_add = True
                    compound = infn_set(j)
                    for t in range(x-1):
                        compound = infn_append(compound,j)
                    continue
                for t in range(x):
                    compound = infn_append(compound,j)
            elif i > 0:
                for t in range(x):
                    mult = infn_mult(j,i)
                    compound = infn_add_extend(compound,mult)

    return H(compound)
                

def informal_matrix_calculator():
    size = int(input("Enter matrix size (e.g., 3 for 3x3): "))
    matrix = []

    for i in range(size):
        row = []
        print(f"Enter row {i+1}:")
        for j in range(size):
            element = int(input(f"Element [{i+1},{j+1}] (+>x): "))
            row.append(element)
        matrix.append(row)

    result = matrix_2d_add_mult_H(matrix, size)
    if result == 0:
        print("invalid matrix!")
    else:
        print(f"result: {result}")


## [WIP] [TODO]
def matrix_3d_add_mult_H(matrix, size):
    # if first row is all 0's matrix is 0
    first_add = False

    sum = 0
    for j in range(size):
        x = matrix[0][j][0]
        if x == 0:
            continue
        sum += x

    if sum == 0:
        return 0

    compound = 0

    for i in range(size):
        for j in range(size):
            for k in range(size):
                if k == 0:
                    x = matrix[i][j][0]
                    if x < 1:
                        continue
                    if i == 0:
                        if first_add == False:
                            first_add = True
                            compound = infn_set(j)
                            for t in range(x-1):
                                compound = infn_append(compound,j)
                            continue
                        for t in range(x):
                            compound = infn_append(compound,j)
                    elif i > 0:
                        for t in range(x):
                            mult = infn_mult(j,i)
                            compound = infn_add_extend(compound,mult)
                elif k > 0:
                    compound = infn_mult_append(compound,k)
                    compound = infn_add_extend(compound,infn_mult(j,i))

    return H(compound)
    
def informal_matrix_calculator_3d():
    size = int(input("Enter matrix size (e.g., 3 for 3x3x3): "))
    matrix = []

    for i in range(size):
        matrix_2d = []
        print(f"Enter elements for 2D slice {i+1} (size: {size}x{size}):")
        for j in range(size):
            row = []
            for k in range(size):
                element = int(input(f"Element [{i+1},{j+1},{k+1}] (+>x): "))
                row.append(element)
            matrix_2d.append(row)
        matrix.append(matrix_2d)

    result = matrix_3d_add_mult_H(matrix, size)
    if result == 0:
        print("Invalid matrix!")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    if "--3d" in sys.argv:
        informal_matrix_calculator_3d()
    else:
        informal_matrix_calculator()
    
