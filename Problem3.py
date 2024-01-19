import numpy as np
import random
def MC_buffon(sims, t, l):
    nbr_strips = np.random.randint(10, 20)
    # x goes from 0 to (nbr_strips - 1) * t
    strips = [t*i for i in range(0, nbr_strips)]
    count = 0
    for _ in range(0, sims):
        x = random.uniform(0, (nbr_strips - 1)*t)
        theta = random.uniform(0, 2)*np.pi
        length = np.abs((l/2)*np.cos(theta))
        x_left = x - length
        x_right = x + length


        for i in range(0, nbr_strips):
            if(x_left < strips[i] and x_right > strips[i]):
                count += 1
                break
    #print(count)       
    return count/sims

t = random.uniform(5, 10) 
l = random.uniform(1, t)*0.7
p = MC_buffon(1000000, t, l)
pi_est = (2/p)*(l/t)

print(f"Estimation of pi {pi_est:.4f}")

