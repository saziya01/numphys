import numpy as np
from pot_well import psi_superposition,normalize_wavefunction,probability_in_half

def test_superposition_normalization_and_probability():
    L = 1.0
    x = np.linspace(0, L, 1000)
    dx = x[1] - x[0]
    
    psi_vals = psi_superposition(x, L)
    normed = normalize_wavefunction(psi_vals, dx)
    
    total_prob = np.sum(np.abs(normed)**2) * dx
    prob_left_half = probability_in_half(normed, dx)
    
    # Test for normalization
    assert np.isclose(total_prob, 1.0, atol=1e-3)
    
    # Test probability in half the box
    assert np.isclose(prob_left_half,0.924413,atol=0.01)