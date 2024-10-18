from itertools import combinations
from itertools import combinations_with_replacement

def infn_set(x):
    """Generate a set of informal numbers based on x."""
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

def infn_mult(x, y):
    """Add two informal sets x and y."""
    set_x = infn_set(x)
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x * num_y)

    return sorted(result)

def infn_mult_append(x, y):
    """Append informal number y to informal set x."""
    set_x = x
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x * num_y)

    return sorted(result)

def infn_mult_extend(informal_set_x, informal_set_y):
    """Append informal number y to informal set."""
    result = set()

    for num_x in informal_set_x:
        for num_y in informal_set_y:
            result.add(num_x * num_y)

    return sorted(result)

def infn_add(x, y):
    """Add two informal sets x and y."""
    set_x = infn_set(x)
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def infn_append(x, y):
    """Append informal number y to informal set x."""
    set_x = x
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)


def infn_add_extend(informal_set_x, informal_set_y):
    """Append informal number y to informal set."""
    result = set()

    for num_x in informal_set_x:
        for num_y in informal_set_y:
            result.add(num_x + num_y)

    return sorted(result)

def H(informal_set):
    """Calculate H from a linear combination of informal numbers and return the informal set."""
    infn = informal_set

    if len(infn) == ((2*max(infn))+1):
        return max(infn)
    return 0


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
                

# Calculator adapted for testing matrix efficiency using informal matrix
def informal_matrix_calculator():
    """Interactive calculator for informal matrix operations."""
    size = int(input("Enter matrix size (e.g., 3 for 3x3): "))
    matrix = []

    # Collect matrix elements from user input
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
    


if __name__ == "__main__":
    informal_matrix_calculator()
