import numpy as np

def psi_superposition(x, L):
    """Superposition of first two eigenstates in a 1D box."""
    return np.sin(np.pi * x / L) + np.sin(2 * np.pi * x / L)

def normalize_wavefunction(psi_values, dx):
    """Normalize a wavefunction using numerical integration."""
    norm = np.sqrt(np.sum(np.abs(psi_values)**2) * dx)
    return psi_values / norm

def probability_in_half(psi_values, dx):
    """Calculate the probability in the left half of the domain."""
    half_index = int(len(psi_values) / 2)
    prob = np.sum(np.abs(psi_values[:half_index])**2) * dx
    return prob