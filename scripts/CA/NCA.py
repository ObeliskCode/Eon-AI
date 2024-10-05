import numpy as np
import matplotlib.pyplot as plt

# Function to generate the infn number set for a given position `x`
def infn_number(x):
    return {-x-1, -x, -x+1, 0, x-1, x, x+1}


def infn_add(x, y):
    set_x = infn_number(x)
    set_y = infn_number(y)

    result = set()

    for num_x in set_x:
        for num_y in set_y:
            result.add(num_x + num_y)

    return sorted(result)

# Function to calculate the next state of a cell based on its current state and its neighbors
def next_cell_state(current_state, neighbor_states):
    alive_neighbors = sum(neighbor_states)
    
    # Apply the 1D Conway's Game of Life rules
    if current_state == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0  # Cell dies
        else:
            return 1  # Cell survives
    else:
        if alive_neighbors == 3:
            return 1  # Cell becomes alive (reproduction)
        else:
            return 0  # Cell stays dead


def next_generation(grid):
    new_grid = np.zeros_like(grid)
    n = len(grid)

    gsize = grid.size
    hwp = (gsize - 1) / 2
    hwpx = -hwp
    
    for i in range(n):
        # try this!
        #infn_set = infn_add((int)(hwpx + i), 3)
        infn_set = infn_number((int)(hwpx + i))

        # Check neighbors based on the infn set
        neighbors = []
        for num_line in infn_set:
            stat = (int)((num_line + hwp))
            if stat > hwp or stat < -hwp:
                continue
            neighbor_index = (int)((num_line + hwp))
            neighbors.append(grid[neighbor_index])
        
        new_grid[i] = next_cell_state(grid[i], neighbors)
    
    return new_grid

def pda_print(g,i):
    gsize = g.size
    hwp = (gsize - 1) / 2
    hwpx = -hwp
    g0 = 0

    for x in g:
        if x == 1:
            g0 += hwpx 
        hwpx += 1
    
    print(g,"| [pda]:",g0,f"| State {i}")

def run_simulation(initial_grid, num_generations):
    grid = initial_grid
    pda_print(grid,0)
    
    state = np.copy(grid)
    history = [state]

    for generation in range(num_generations):
        grid = next_generation(grid)
        pda_print(grid,generation+1)
        history.append(np.copy(grid))
    
    history = np.array(history)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(history, cmap='binary', interpolation='nearest', aspect='auto')
    plt.xlabel("index")
    plt.ylabel("generations")
    plt.title(f"Noel's Game of Life")
    plt.show()

    return grid

# grid should always have an odd size!
#initial_grid = np.array([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0])
initial_grid = np.random.randint(0, 2, size=10000)

final_grid = run_simulation(initial_grid, num_generations=10)
