def oblong_addition(a, b, c, d):
    return (a + c, b + d)

# Example usage
result = oblong_addition(3, 4, 1, 2)
print("Addition Result:", result)

def oblong_multiplication(a, b, c, d):
    return (a * c - b * d, a * d + b * c)

# Example usage
result = oblong_multiplication(3, 4, 1, 2)
print("Multiplication Result:", result)

def informal_number_operations(c, d, e, f):
    # Assumes d and f are restricted to rationals
    result_add = (c + e, d + f)
    result_multiply = (c * e - d * f, c * f + d * e)
    return result_add, result_multiply

# Example usage
add_result, multiply_result = informal_number_operations(2, 1, 3, 0.5)
print("Informal Addition Result:", add_result)
print("Informal Multiplication Result:", multiply_result)
