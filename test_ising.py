# test_ising_model.py
import numpy as np
from ising_model import (
    calculate_energy,
    calculate_magnetization,
    run_ising_simulation,
    plot_results
)

def test_calculate_energy_all_up():
    spins = np.ones(10, dtype=int)
    assert np.isclose(calculate_energy(spins, J=1), -1.0)

def test_calculate_energy_alternating():
    spins = np.array([1, -1] * 5)
    assert np.isclose(calculate_energy(spins, J=1), 1.0)

def test_calculate_magnetization_all_down():
    spins = -np.ones(10, dtype=int)
    assert np.isclose(calculate_magnetization(spins), 1.0)

def test_calculate_magnetization_half_up_half_down():
    spins = np.array([1, -1] * 5)
    assert np.isclose(calculate_magnetization(spins), 0.0)

def test_run_ising_simulation_output_keys():
    result = run_ising_simulation(N=10, MCS=100, temperature_range=np.linspace(1, 2, 3))
    expected_keys = {
        "temperature_range", "average_energies", "average_magnetizations",
        "specific_heats", "magnetic_susceptibility"
    }
    assert expected_keys.issubset(result.keys())

def test_run_ising_simulation_output_lengths():
    T_range = np.linspace(1, 2, 5)
    result = run_ising_simulation(N=10, MCS=100, temperature_range=T_range)
    for key in ["average_energies", "average_magnetizations", "specific_heats", "magnetic_susceptibility"]:
        assert len(result[key]) == len(T_range)

# This test now shows plots on screen (no mocking)
def test_plot_results_show_graph():
    T_range = np.linspace(0.1, 5, 50)
    result = run_ising_simulation(N=50, MCS=500, temperature_range=T_range)
    plot_results(result)  # This will display the plots