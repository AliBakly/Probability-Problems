import numpy as np
def simulation(m, n, sim):
    # m: number of white to begin with
    # n: number of black to begin with
    # sim: number of simulations
    elements = [0, 1] # Represent white as 0 and black as 1
    total_white = 0 # Number of simulations where all are white
    
    for _ in range(sim):
        white_counter = m     
        black_counter = n
        while(white_counter != 0 and black_counter != 0):
            probabilities = [white_counter/(white_counter + black_counter), 1 - white_counter/(white_counter + black_counter)]
            color = np.random.choice(elements, 1, p=probabilities)
            
            if(color == 0):
                white_counter = white_counter - 1
            else:
                white_counter = white_counter + 1
                black_counter = black_counter - 1

        if(black_counter == 0):
            total_white = total_white + 1
    return total_white/sim

print(f"White ratio: {simulation(1,1000,1000) :.3f}")

