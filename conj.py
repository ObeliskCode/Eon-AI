# conj.py

# R-Algebra operations implementation

# Function for Oblong Addition
def oblong_addition(a, b, c, d):
    return (a + c, b + d)

# Function for Oblong Subtraction
def oblong_subtraction(a, b, c, d):
    return (a - c, b - d)

# Function for Oblong Multiplication
def oblong_multiplication(a, b, c, d):
    return (a * c - b * d, a * d + b * c)

# Function for Oblong Division
def oblong_division(a, b, c, d):
    denominator = c**2 + d**2
    return ((a * c + b * d) / denominator, (b * c - a * d) / denominator)

# Function for Informal Number operations (addition and multiplication)
def informal_number_operations(c, d, e, f):
    # Assumes d and f are restricted to rationals
    result_add = (c + e, d + f)
    result_multiply = (c * e - d * f, c * f + d * e)
    return result_add, result_multiply

# Testing framework for R-Algebra functions
def run_tests():
    # Test Oblong Addition
    assert oblong_addition(3, 4, 1, 2) == (4, 6), "Test failed for oblong_addition"
    print("Oblong Addition Test Passed!")

    # Test Oblong Subtraction
    assert oblong_subtraction(3, 4, 1, 2) == (2, 2), "Test failed for oblong_subtraction"
    print("Oblong Subtraction Test Passed!")

    # Test Oblong Multiplication
    assert oblong_multiplication(3, 4, 1, 2) == (-5, 10), "Test failed for oblong_multiplication"
    print("Oblong Multiplication Test Passed!")

    # Test Oblong Division
    div_result = oblong_division(3, 4, 1, 2)
    expected_div_result = (2.2, 0.4)  # Approximate expected values
    assert abs(div_result[0] - expected_div_result[0]) < 1e-10, "Test failed for oblong_division"
    assert abs(div_result[1] - expected_div_result[1]) < 1e-10, "Test failed for oblong_division"
    print("Oblong Division Test Passed!")

    # Test Informal Number Operations
    add_result, multiply_result = informal_number_operations(2, 1, 3, 0.5)
    assert add_result == (5, 1.5), "Test failed for informal_number_addition"
    assert multiply_result == (6, 0.5), "Test failed for informal_number_multiplication"
    print("Informal Number Operations Test Passed!")

def calculator():
    print("+",oblong_addition(3, 4, 1, 2))
    print("-",oblong_subtraction(3, 4, 1, 2))
    print("*",oblong_multiplication(3, 4, 1, 2))
    print("/",oblong_division(3, 4, 1, 2))


# Main function to execute the tests
if __name__ == "__main__":
    calculator()
