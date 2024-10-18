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
            result.mult(num_x * num_y)

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

def H(informal_combination):
    """Calculate H from a linear combination of informal numbers and return the informal set."""
    informal_nums = []
    infn = set()
    
    # Generate informal sets for each number in the informal combination
    for num in informal_combination:
        informal_nums.append(infn_set(num))  # Create an informal set for each number

     # Start with the first informal number set
    if len(informal_nums) > 0:
        infn = informal_nums[0]

    for infn_x in informal_nums[1:]:
        infn = infn_add_extend(infn, infn_x)  # Use infn_append to build the set

    total = sum(infn)  # Calculate total of the combined informal set

    # Check if the total sum is zero
    if total == 0:
        # Return the maximum element from the combined informal set
        return max(infn)
    
    # Return the total if it is not zero
    return total


def matrix_2d_add_mult_H(matrix, size):
    # if first row is all 0's matrix is 0
    first_add = False
    
    sum = 0
    for j in range(size):
        x = matrix[0][j]
        if x == 0:
            continue
        sum += x
        if first_add = False:
            first_add = True
            compound = infn_set(j)
            matrix[0][j] = x - 1

    if sum == 0:
        return 0

    for i in range(size):
        for j in range(size):
            x = matrix[i][j]
            if x == 0:
    
    return 0
                

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
    print(f"result: {result}")
    


if __name__ == "__main__":
    informal_matrix_calculator()
