import numpy as np

def sample_spherical(npoints, radius, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    vec *= np.sqrt(radius)
    return vec

def same_side(v1, v2, v3, v4, p):
    normal = np.cross(v2 - v1, v3 - v1)
    dotV4 = np.dot(normal, v4 - v1)
    dotP = np.dot(normal, p - v1)
    return np.sign(dotV4) == np.sign(dotP)

def point_in_tetrahedron(v1, v2, v3, v4, p):
    return same_side(v1, v2, v3, v4, p) and\
           same_side(v2, v3, v4, v1, p) and\
           same_side(v3, v4, v1, v2, p) and\
           same_side(v4, v1, v2, v3, p)

def sim_prob(radius, sims):
    center = [0, 0, 0]
    counter = 0
    for _ in range(0, sims):
        vec = np.transpose(sample_spherical(4, radius))
        if point_in_tetrahedron(vec[0], vec[1], vec[2], vec[3], center):
            counter += 1
    return counter/sims

p = sim_prob(1, 100000)
print(f"Probability of center being inside tetrahedron: {p :4f}")