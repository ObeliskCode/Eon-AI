def infn_set(x):
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

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

def calculator():
    start_x = int(input("Enter the first infn number +>x: "))
    start_y = int(input("Enter the second infn number +>y: "))
    
    final_result = infn_add(start_x, start_y)
    
    print(f"+>{start_x} + +>{start_y} = {sorted(final_result)}")

    while(True):
        z = int(input("Enter the x infn number +>z: "))
        final_result = infn_append(final_result, z)
        print(f"... + +>{z} = {sorted(final_result)}")

if __name__ == "__main__":
    calculator()
