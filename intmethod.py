import numpy as np

def f(x):
    """Function to integrate: sin(x)"""
    return np.sin(x)

def trapezoidal_integration(y,a, b, h):
    """Numerical integration using the trapezoidal rule."""
    n = int((b - a) / h) + 1
    x = np.linspace(a, b, n)
    y = f(x)
    
    sum_y = np.sum(y[1:-1])  # Sum of y[i] for i from 1 to n-2
    I = (h / 2) * (y[0] + y[-1] + 2 * sum_y)
    
    return I

def simpsons_rule(y,a, b, n):
    """Numerical integration using Simpson's rule."""
    if n % 2 == 1:  # Ensure n is even
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    I = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    
    return I
