# div.py

# R-Algebra operations implementation

# Function for infn Addition
def infn_add_sub(a, b, c, d):
    return (a + c, b + d)

# Function for infn Multiplication
def infn_mult_div(a, b, c, d):
    return (a * c - b * d, a * d + b * c)

# Function for Informal Number operations (addition and multiplication)
def informal_number_operations(c, d, e, f):
    # Assumes d and f are restricted to rationals
    result_add = (c + e, d + f)
    result_multiply = (c * e - d * f, c * f + d * e)
    return result_add, result_multiply

def calculator():
    print("+- | */", informal_number_operations(3, 4, 1, 2))

# Main function to execute the tests
if __name__ == "__main__":
    calculator()
