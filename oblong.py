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

def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number.
    """
    fib = [0, 1]
    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

def repeated_fib_oblong_additions(max_fib):
    """
    Performs oblong additions for Fibonacci numbers up to `max_fib`.
    """
    fib_seq = fibonacci_sequence(max_fib)
    print(f"Fibonacci sequence (up to {max_fib}): {fib_seq}")

    result_set = oblong_add(fib_seq[0], fib_seq[1])
    print(f"Initial oblong Addition >{fib_seq[0]} + >{fib_seq[1]}: {result_set}")
    
    for i in range(2, max_fib):
        next_oblong = fib_seq[i]
        result_set = oblong_add(fib_seq[i-1], next_oblong)
        print(f"(Adding >{next_oblong}): {result_set}")

    return result_set

def main():
    start_x = int(input("Enter the first oblong number >x: "))
    start_y = int(input("Enter the second oblong number >y: "))
    
    final_result = oblong_add(start_x, start_y)
    
    print(f"+>{start_x} + +>{start_y} = {sorted(final_result)}")

    max_fib = int(input("Enter the number of Fibonacci oblong additions: "))
    
    final_result = repeated_fib_oblong_additions(max_fib)
    
    print(f"Final result after {max_fib} Fibonacci-based additions: {final_result}")

if __name__ == "__main__":
    main()
