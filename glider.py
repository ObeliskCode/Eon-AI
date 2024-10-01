class GliderNumber:
    def __init__(self, x):
        self.x = x
        self.set_rep = {-(x + 1), -x, -(x - 1), 0, x - 1, x, x + 1}

    def __add__(self, other):
        return self.set_rep.union(other.set_rep)

    def __sub__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"Glider >{self.x} is represented by the set: {sorted(self.set_rep)}"

def glider_addition(x, y):
    glider_x = GliderNumber(x)
    glider_y = GliderNumber(y)
    
    result_addition = glider_x + glider_y
    result_subtraction = glider_x - glider_y
    
    print(f"Glider >{x} + Glider >{y} results in the set: {sorted(result_addition)}")
    print(f"Glider >{x} - Glider >{y} results in the set: {sorted(result_subtraction)}")

glider_addition(3, 5)
