from itertools import combinations
from itertools import combinations_with_replacement

def infn_set(x):
    """Generate a set of informal numbers based on x."""
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

def infn_mult(x, y):
    """Add two informal sets x and y."""
    set_x = infn_set(x)
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.mult(num_x * num_y)

    return sorted(result)

def infn_mult_append(x, y):
    """Append informal number y to informal set x."""
    set_x = x
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x * num_y)

    return sorted(result)

def infn_mult_extend(informal_set_x, informal_set_y):
    """Append informal number y to informal set."""
    result = set()

    for num_x in informal_set_x:
        for num_y in informal_set_y:
            result.add(num_x * num_y)

    return sorted(result)

def infn_add(x, y):
    """Add two informal sets x and y."""
    set_x = infn_set(x)
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

def infn_append(x, y):
    """Append informal number y to informal set x."""
    set_x = x
    set_y = infn_set(y)

    result = set()
    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)


def infn_add_extend(informal_set_x, informal_set_y):
    """Append informal number y to informal set."""
    result = set()

    for num_x in informal_set_x:
        for num_y in informal_set_y:
            result.add(num_x + num_y)

    return sorted(result)

def calculator():
    """Interactive calculator for adding informal numbers."""
    inp = ''
    z = 0
    inp = input("infn number +>x (q to quit): ")
    if inp == 'q':
        return -1
    z = int(inp)
    start_x = z
    inp = input("infn number +>y (q to quit): ")
    if inp == 'q':
        ret = infn_set(start_x)
        print(f"+>{start_x} = {sorted(ret)}")
        return ret
    z = int(inp)
    start_y = z
    
    final_result = infn_add(start_x, start_y)
    print(f"+>{start_x} + +>{start_y} = {sorted(final_result)}")

    while True:
        inp = input("Enter +>z (type -x to multiply) (q to quit): ")
        if inp == 'q':
            break
        z = int(inp)
        if z < 0:
            mult_scalar = -z
            inp = input(f"Enter the integer scalar for +>{mult_scalar}: ")
            scalar = int(inp)
            ## do scalar math.
            if scalar == 1:
                final_result = infn_mult_append(final_result, mult_scalar)
            elif scalar > 1:
                compound = infn_add(mult_scalar, mult_scalar)
                for i in range(scalar):
                    if i < 2:
                        continue
                    compound = infn_append(compound,mult_scalar)
                final_result = infn_mult_extend(final_result, compound)
            print(f"... x ({scalar})+>{z} = {sorted(final_result)}")
            continue
        final_result = infn_append(final_result, z)
        print(f"... + +>{z} = {sorted(final_result)}")
    
    return final_result

if __name__ == "__main__":
    calculator()
