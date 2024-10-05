from itertools import combinations

def generate_informal_numbers(limit):
    """Generate informal numbers in the range -limit to limit."""
    return list(range(-limit, limit + 1))

def check_equality(numbers):
    """Check for equality among all combinations of informal numbers."""
    results = {}
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            combo_sorted = tuple(sorted(combo))
            if combo_sorted not in results:
                results[combo_sorted] = True  # Unique combination found
    return results

def find_geometric_patterns(numbers, target_sum):
    """Find geometric patterns of integers that add up to a minimized sum."""
    results = []
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target_sum:
                results.append(combo)
    return results

def main():
    # Define the limit for informal numbers and target sum
    limit = 10000
    target_sum = 0  # You can modify this to set the desired sum
    informal_numbers = generate_informal_numbers(limit)
    
    # Check equality of combinations
    equality_results = check_equality(informal_numbers)
    total_unique_combinations = len(equality_results)
    print(f'Total unique combinations found: {total_unique_combinations}')
    
    # Find geometric patterns for the given target sum
    geometric_patterns = find_geometric_patterns(informal_numbers, target_sum)
    print(f'Geometric patterns that add up to {target_sum}: {geometric_patterns}')

if __name__ == "__main__":
    main()
