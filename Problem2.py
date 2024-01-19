import numpy as np
def two_same_birthday_prob(nbr_persons, nbr_share, sim):
    found = 0
    for _ in range(0, sim):
        days = np.random.randint(0, 365, size=nbr_persons)
        days.sort()
        for i in range(0, nbr_persons - (nbr_share - 1)):
            if(days[i] == days[i + (nbr_share - 1)]):
                found +=1
                break
    return found/sim
            
nbr_persons = 23
nbr_share = 2
sims = 100000
prob = two_same_birthday_prob(nbr_persons, nbr_share, sims)

print(f"Probability of {nbr_share} out of {nbr_persons} persons sharing the same dat: {prob:.3f}")
