from infmath import *

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
