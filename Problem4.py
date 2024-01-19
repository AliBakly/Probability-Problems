import numpy as np
def random_walk(org, sims, steps, dims):
    count = 0
    
    for _ in range(0, sims):
        current_point = org.copy()
        dim_step = np.random.randint(0, dims, size=steps) # 0, 1, 2, ..., dims-1
        step = 2*np.random.randint(0, 2, size =steps) - 1 # -1 or 1
        
        for i in range(0,steps):
            current_point[dim_step[i]] = current_point[dim_step[i]] + step[i]
            if(current_point == org):
                count += 1
                break
                
    return count/sims

org =[0,0,0]
sims = 5000
steps = 50000
dims = 3
p = random_walk(org, sims, steps, dims)
print(f"Probability of returning to origin: {p}")
