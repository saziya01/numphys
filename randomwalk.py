import random

def single_random_walk(n_steps):
    position = 0
    trajectory = [position]
    for _ in range(n_steps):
        step = 1 if random.random() > 0.5 else -1
        position += step
        trajectory.append(position)
    return trajectory

def multiple_random_walks(n_steps, n_walkers):
    all_trajectories = []
    for _ in range(n_walkers):
        all_trajectories.append(single_random_walk(n_steps))
    return all_trajectories

def random_walk_statistics(n_steps, n_walkers):
    final_positions = []
    for _ in range(n_walkers):
        position = 0
        for _ in range(n_steps):
            step = 1 if random.random() > 0.5 else -1
            position += step
        final_positions.append(position)
    return final_positions