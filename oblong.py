def glider_set(x):
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

def glider_add(x, y):
    set_x = glider_set(x)
    set_y = glider_set(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number.
    """
    fib = [0, 1]
    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

def repeated_fib_glider_additions(max_fib):
    """
    Performs Glider additions for Fibonacci numbers up to `max_fib`.
    """
    fib_seq = fibonacci_sequence(max_fib)
    print(f"Fibonacci sequence (up to {max_fib}): {fib_seq}")

    result_set = glider_add(fib_seq[0], fib_seq[1])
    print(f"Initial Glider Addition >{fib_seq[0]} + >{fib_seq[1]}: {result_set}")
    
    for i in range(2, max_fib):
        next_glider = fib_seq[i]
        result_set = glider_add(fib_seq[i-1], next_glider)
        print(f"(Adding >{next_glider}): {result_set}")

    return result_set

def main():
    start_x = int(input("Enter the first Glider number >x: "))
    start_y = int(input("Enter the second Glider number >y: "))
    
    final_result = glider_add(start_x, start_y)
    
    print(f">x + >y: {sorted(final_result)}")

    max_fib = int(input("Enter the number of Fibonacci Glider additions: "))
    
    final_result = repeated_fib_glider_additions(max_fib)
    
    print(f"Final result after {max_fib} Fibonacci-based additions: {final_result}")

if __name__ == "__main__":
    main()
