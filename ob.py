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

def main():
    start_x = int(input("Enter the first oblong number +>x: "))
    start_y = int(input("Enter the second oblong number +>y: "))
    
    final_result = oblong_add(start_x, start_y)
    
    print(f"+>{start_x} + +>{start_y} = {sorted(final_result)}")

    while(True):
        z = int(input("Enter the x oblong number +>z: "))
        final_result = oblong_append(final_result, z)
        print(f"... + +>{z} = {sorted(final_result)}")

if __name__ == "__main__":
    main()
