from itertools import combinations

# Function to generate informal numbers in the range -limit to limit
def generate_informal_numbers(limit):
    return list(range(-limit, limit + 1))

# Function to check for equality among all combinations of informal numbers
def check_equality(numbers):
    results = {}
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            combo_sorted = tuple(sorted(combo))
            if combo_sorted not in results:
                results[combo_sorted] = True  # Unique combination found
    return results

# Function to find geometric patterns of integers that add up to a minimized sum
def find_geometric_patterns(numbers, target_sum):
    results = []
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target_sum:
                results.append(combo)
    return results

# Define the limit for informal numbers and target sum
limit = 4  # Reduced for performance
target_sum = 0  # Set the desired sum

# Generate informal numbers
informal_numbers = generate_informal_numbers(limit)

# Check equality of combinations
equality_results = check_equality(informal_numbers)
total_unique_combinations = len(equality_results)

# Find geometric patterns for the given target sum
geometric_patterns = find_geometric_patterns(informal_numbers, target_sum)

print(total_unique_combinations, len(geometric_patterns), geometric_patterns)  # Displaying first 5 results
