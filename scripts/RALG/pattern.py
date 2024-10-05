from itertools import combinations

def oblong_set(x):
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

def oblong_add(x, y):
    set_x = oblong_set(x)
    set_y = oblong_set(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def oblong_append(x, y):
    set_x = x
    set_y = oblong_set(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def find_informal_sets(combinations, target):
    """Generate list of numbers for analysis."""
    # [TODO]

    return
    

def check_equality(numbers, target):
    """Check for equality among all combinations of informal numbers."""
    infn = set()
    
    for o in range(len(numbers)):
        if o == 0:
            infn = oblong_add(numbers[0],numbers[1])
        else if o == 1:
            continue
        else:
            infn = oblong_append(infn,numbers[o])

    if infn == oblong_set(target):
        return True
    else:
        return False

def main():
    # Define the limit for informal numbers and target sum
    combinations = 4
    target_infn = 5  # You can modify this to set the desired sum
    
    # Check equality of combinations
    informal_sets = find_informal_sets(combinations, target_infn)
    total_unique_combinations = len(informal_sets)
    print(f'combinations for {target_infn} up to {combinations} slots: {total_unique_combinations}')
    print(f'{informal_sets}')

if __name__ == "__main__":
    main()
