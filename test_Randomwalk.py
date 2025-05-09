import matplotlib.pyplot as plt
import numpy as np
from randomwalk import single_random_walk , multiple_random_walks , random_walk_statistics

def test_main():
    method = input("Choose method (1Dsingle / 1Dmultiple / 1Dstat): ").strip().lower()
    n_steps = int(input("Enter number of steps: "))
    n_walkers = int(input("Enter number of walkers: "))

    if method == "1dsingle":
        traj = single_random_walk(n_steps)
        plt.plot(traj)
        plt.title("1D Random Walk - Single Trajectory")
        plt.xlabel("Step")
        plt.ylabel("Position")
        plt.grid()
        plt.show()

    elif method == "1dmultiple":
        all_traj = multiple_random_walks(n_steps, n_walkers)
        for traj in all_traj:
            plt.plot(traj, alpha=0.5)
        plt.title(f"1D Random Walk - {n_walkers} Walkers")
        plt.grid()
        plt.show()

    elif method == "1dstat":
        positions = random_walk_statistics(n_steps, n_walkers)
        print(f"Mean: {np.mean(positions)}")
        print(f"Std Dev: {np.std(positions)}")
        print(f"Variance: {np.var(positions)}")
        plt.hist(positions, bins=20)
        plt.title("Histogram of Final Positions")
        plt.grid()
        plt.show()
    else:
        print("Invalid method.")

if __name__ == "__main__":
   test_main()