#this code is for estimation of pie value using monter carlo


import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

# Number of random points



