from itertools import combinations

def infn_set(x):
    return sorted(set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1]))

def infn_add(x, y):
    set_x = infn_set(x)
    set_y = infn_set(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def infn_append(x, y):
    set_x = x
    set_y = infn_set(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def find_informal_sets(combo_length, target):
    """Generate list of numbers for analysis."""
    informal_sets = []
    
    # Consider numbers from 1 to some arbitrary limit for now (you can change the limit as desired)
    numbers = list(range(1, 10))  # Modify range as needed for your use case
    
    # Iterate over all combinations of 'combo_length' length
    for i in range(combo_length):
        if i < 2:
            continue
        for combo in combinations(numbers, i):
            # Check if this combination satisfies the target using check_equality
            if check_equality(combo, target):
                informal_sets.append(combo)

    return informal_sets

def check_equality(numbers, target):
    """Check for equality among all combinations of informal numbers."""
    infn = set()
    
    for o in range(len(numbers)):
        if o == 0:
            infn = infn_add(numbers[0],numbers[1])
        elif o == 1:
            continue
        else:
            infn = infn_append(infn,numbers[o])

    if infn == target:
        return True
    else:
        return False

def main():
    # Define the limit for informal numbers and target sum
    combo_length = 10  # Adjust the number of slots
    target_infset = infn_append(infn_add(5,5),5) # You can modify this to set the desired target sum
    
    # Check equality of combinations
    informal_sets = find_informal_sets(combo_length, target_infset)
    total_unique_combinations = len(informal_sets)
    print(f'Combinations for {target_infset} up to {combo_length} slots: {total_unique_combinations}')
    print(f'{informal_sets}')

if __name__ == "__main__":
    main()
