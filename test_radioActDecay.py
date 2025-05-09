import matplotlib.pyplot as plt
from radioactivedecay import simulate_decay

def test_main():
    A0 = int(input("Enter A Concentraction :"))
    B0 = int(input("Enter B Concentraction :"))
    k = float(input("Enter rate constant :"))
    t_range = (0, 50, 1000)  # (start, end, num_points)

    t, sol = simulate_decay(A0, B0, k, t_range)

    plt.plot(t, sol[:, 0], label='A(t)')
    plt.plot(t, sol[:, 1], label='B(t)')
    plt.xlabel('Time (t)')
    plt.ylabel('Number of molecules')
    plt.title('Radioactive Decay Simulation')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
   test_main()