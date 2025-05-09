# ising_model.py
import numpy as np
import matplotlib.pyplot as plt

def calculate_energy(spins, J=1):
    N = len(spins)
    return -J * np.sum(spins * np.roll(spins, 1)) / N  

def calculate_magnetization(spins):
    return np.abs(np.sum(spins)) / len(spins)

def run_ising_simulation(N=100, J=1, MCS=10000, temperature_range=None):
    if temperature_range is None:
        temperature_range = np.linspace(0.1, 10, 100)

    average_energies = []
    average_magnetizations = []
    specific_heats = []
    mag_susceptibility = []

    for T in temperature_range:
        beta = 1 / T
        spins = -np.ones(N, dtype=int)

        for _ in range(MCS):
            i = np.random.randint(0, N)
            delta_E = 2 * J * spins[i] * (spins[(i - 1) % N] + spins[(i + 1) % N])
            if delta_E <= 0 or np.random.rand() < np.exp(-delta_E * beta):
                spins[i] *= -1

        energy_samples = []
        magnetization_samples = []

        for _ in range(1000):
            i = np.random.randint(0, N)
            delta_E = 2 * J * spins[i] * (spins[(i - 1) % N] + spins[(i + 1) % N])
            if delta_E <= 0 or np.random.rand() < np.exp(-delta_E * beta):
                spins[i] *= -1

            energy_samples.append(calculate_energy(spins, J))
            magnetization_samples.append(calculate_magnetization(spins))

        avg_energy = np.mean(energy_samples)
        sq_energy = np.mean(np.array(energy_samples)**2)
        avg_magnetization = np.mean(magnetization_samples)
        sq_mag = np.mean(np.array(magnetization_samples)**2)

        specific_heat = (sq_energy - avg_energy*2) / (T*2)
        mag_sus = (sq_mag - avg_magnetization**2) / T

        average_energies.append(avg_energy)
        average_magnetizations.append(avg_magnetization)
        specific_heats.append(specific_heat)
        mag_susceptibility.append(mag_sus)

    return {
        "temperature_range": temperature_range,
        "average_energies": average_energies,
        "average_magnetizations": average_magnetizations,
        "specific_heats": specific_heats,
        "magnetic_susceptibility": mag_susceptibility,
    }

def plot_results(results):
    T = results["temperature_range"]
    E = results["average_energies"]
    M = results["average_magnetizations"]
    Cv = results["specific_heats"]
    X = results["magnetic_susceptibility"]

    plt.figure()
    plt.plot(T, E)
    plt.xlabel("Temperature (T)")
    plt.ylabel("Average Energy")
    plt.title("Energy vs. Temperature in 1D Ising Model")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(T, M)
    plt.xlabel("Temperature (T)")
    plt.ylabel("Average Magnetization")
    plt.title("Magnetization vs. Temperature in 1D Ising Model")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(T, Cv)
    plt.xlabel("Temperature (T)")
    plt.ylabel("Specific Heat (Cv)")
    plt.title("Cv vs. Temperature")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(T, X)
    plt.xlabel("Temperature (T)")
    plt.ylabel("Magnetic Susceptibility")
    plt.title("Magnetic Susceptibility vs. Temperature")
    plt.grid(True)

    plt.tight_layout()
    plt.show()