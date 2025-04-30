import sympy as sp

def bisection(func_str, a, b, tol=1e-6, max_iter=100, verbose=False):
    x = sp.symbols('x')
    func = sp.sympify(func_str)

    if func.subs(x, a) * func.subs(x, b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    for i in range(max_iter):
        c = (a + b) / 2
        if verbose:
            print(f"Bisection Iteration {i+1}: a={a}, b={b}, c={c}, f(c)={func.subs(x, c)}")

        if abs(func.subs(x, c)) < tol or (b - a) / 2 < tol:
            return c

        if func.subs(x, c) * func.subs(x, a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def false_position(func_str, a, b, tol=1e-6, max_iter=100, verbose=False):
    x = sp.symbols('x')
    func = sp.sympify(func_str)

    if func.subs(x, a) * func.subs(x, b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    for i in range(max_iter):
        fa = func.subs(x, a)
        fb = func.subs(x, b)
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = func.subs(x, c)
        
        if verbose:
            print(f"False Position Iteration {i+1}: a={a}, b={b}, c={c}, f(c)={fc}")

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    return (a * func.subs(x, b) - b * func.subs(x, a)) / (func.subs(x, b) - func.subs(x, a))


def newton_raphson(func_str, x0, tol=1e-6, max_iter=100, verbose=False):
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    dfunc = sp.diff(func, x)   # Derivative

    for i in range(max_iter):
        f_val = func.subs(x, x0)
        df_val = dfunc.subs(x, x0)

        if df_val == 0:
            raise ZeroDivisionError("Derivative became zero. Newton-Raphson failed.")

        x1 = x0 - f_val / df_val
        
        if verbose:
            print(f"Newton-Raphson Iteration {i+1}: x0={x0}, f(x0)={f_val}, f'(x0)={df_val}, x1={x1}")

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1

    return x0
