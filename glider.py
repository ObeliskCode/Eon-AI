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

def main():
    start_x = int(input("Enter the first Glider number >x: "))
    start_y = int(input("Enter the second Glider number >y: "))
    
    final_result = glider_add(start_x, start_y)
    
    print(f">x + >y: {sorted(final_result)}")

if __name__ == "__main__":
    main()
