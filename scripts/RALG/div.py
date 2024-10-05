# div.py

# R-Algebra operations implementation

# Function for infn Addition
def infn_addition(a, b, c, d):
    return (a + c, b + d)

# Function for infn Subtraction
def infn_subtraction(a, b, c, d):
    return (a - c, b - d)

# Function for infn Multiplication
def infn_multiplication(a, b, c, d):
    return (a * c - b * d, a * d + b * c)

# Function for infn Division
def infn_division(a, b, c, d):
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
    # Test infn Addition
    assert infn_addition(3, 4, 1, 2) == (4, 6), "Test failed for infn_addition"
    print("infn Addition Test Passed!")

    # Test infn Subtraction
    assert infn_subtraction(3, 4, 1, 2) == (2, 2), "Test failed for infn_subtraction"
    print("infn Subtraction Test Passed!")

    # Test infn Multiplication
    assert infn_multiplication(3, 4, 1, 2) == (-5, 10), "Test failed for infn_multiplication"
    print("infn Multiplication Test Passed!")

    # Test infn Division
    div_result = infn_division(3, 4, 1, 2)
    expected_div_result = (2.2, 0.4)  # Approximate expected values
    assert abs(div_result[0] - expected_div_result[0]) < 1e-10, "Test failed for infn_division"
    assert abs(div_result[1] - expected_div_result[1]) < 1e-10, "Test failed for infn_division"
    print("infn Division Test Passed!")

    # Test Informal Number Operations
    add_result, multiply_result = informal_number_operations(2, 1, 3, 0.5)
    assert add_result == (5, 1.5), "Test failed for informal_number_addition"
    assert multiply_result == (6, 0.5), "Test failed for informal_number_multiplication"
    print("Informal Number Operations Test Passed!")

def calculator():
    print("+",infn_addition(3, 4, 1, 2))
    print("-",infn_subtraction(3, 4, 1, 2))
    print("*",infn_multiplication(3, 4, 1, 2))
    print("/",infn_division(3, 4, 1, 2))


# Main function to execute the tests
if __name__ == "__main__":
    calculator()
