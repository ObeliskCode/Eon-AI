from itertools import combinations

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

def infn_div(x, y):
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

def find_informal_sets(combo_length, target):
    """Generate combinations of informal numbers that equal the target."""
    informal_sets = []
    numbers = list(range(1, combo_length))  # Modify range as needed for your use case
    
    # Iterate over all combinations of 'combo_length'
    for i in range(2, combo_length + 1):
        for combo in combinations(numbers, i):
            if check_equality(combo, target):
                informal_sets.append(combo)

    return informal_sets

def check_equality(numbers, target):
    """Check if a combination of informal numbers equals the target."""
    infn = set()
    
    for o in range(len(numbers)):
        if o == 0:
            infn = infn_add(numbers[0], numbers[1])
        elif o == 1:
            continue
        else:
            infn = infn_append(infn, numbers[o])

    return infn == target

def calculator():
    """Interactive calculator for adding informal numbers."""
    start_x = int(input("Enter the first infn number +>x: "))
    start_y = int(input("Enter the second infn number +>y: "))
    
    final_result = infn_add(start_x, start_y)
    print(f"+>{start_x} + +>{start_y} = {sorted(final_result)}")

    while True:
        z = int(input("Enter the x infn number +>z (or type -1 to finish): "))
        if z == -1:
            break
        final_result = infn_append(final_result, z)
        print(f"... + +>{z} = {sorted(final_result)}")
    
    return final_result

def main():
    target = calculator()
    
    combo_length = int(input("Enter combo length to search: "))

    informal_combinations = find_informal_sets(combo_length, target)
    
    print("Informal Combinations that equal the target:")
    for combo in informal_combinations:
        h_value = H(combo)  # Calculate H for each valid combination
        print(f"{combo} => H = {h_value}")

if __name__ == "__main__":
    main()
