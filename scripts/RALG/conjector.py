from itertools import combinations

def infn_set(x):
    """Generate a set of informal numbers based on x."""
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

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

    combination = find_informal_sets(combo_length, target)
    
    if combination:
        print(combination)
    else:
        print(f'No combinations found.')

if __name__ == "__main__":
    main()
