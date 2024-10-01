def glider_set(x):
    return set([-x - 1, -x, -x + 1, 0, x - 1, x, x + 1])

#[todo] fix glider add function
def glider_add(x, y):
    set_x = glider_set(x)
    set_y = glider_set(y)
    return set_x.union(set_y) # not correct

def main():
    start_x = int(input("Enter the first Glider number >x: "))
    start_y = int(input("Enter the second Glider number >y: "))
    
    final_result = glider_add(start_x, start_y)
    
    print(f">x + >y: {sorted(final_result)}")

# Run the program
if __name__ == "__main__":
    main()
