def glider_set(x):
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

def glider_add(x, y):
    set_x = glider_set(x)
    set_y = glider_set(y)
    return set_x.union(set_y)

def repeated_glider_additions(start_x, start_y, max_additions):
    result_set = glider_add(start_x, start_y)
    print(f"Initial Glider Addition >{start_x} + >{start_y}: {sorted(result_set)}")
    
    for i in range(2, max_additions + 1):
        next_glider = i
        result_set = result_set.union(glider_set(next_glider))
        print(f"After {i} Glider Additions (Adding >{next_glider}): {sorted(result_set)}")

    return result_set

def main():
    start_x = int(input("Enter the first Glider number >x: "))
    start_y = int(input("Enter the second Glider number >y: "))
    max_additions = int(input("Enter the maximum number of Glider additions: "))
    
    final_result = repeated_glider_additions(start_x, start_y, max_additions)
    
    print(f"Final result after {max_additions} additions: {sorted(final_result)}")

# Run the program
if __name__ == "__main__":
    main()
