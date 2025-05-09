import numpy as np
from scipy.integrate import odeint

def decay_model(y, t, k):
    A, B = y
    dAdt = -k * A
    dBdt = k * A
    return [dAdt, dBdt]

def simulate_decay(A0, B0, k, t_range):
    y0 = [A0, B0]
    t = np.linspace(*t_range)
    sol = odeint(decay_model, y0, t, args=(k,))
    return t,sol