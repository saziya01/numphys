import sympy as sp
import numpy as np
import math

def find_root(func_str, a, b, method, maxiter):
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    f = sp.lambdify(x, func, modules=["numpy"])
    df = sp.lambdify(x, sp.diff(func, x), modules=["numpy"])
    table = []

    def bisection(a, b, maxiter, tol=1e-6):
        for i in range(maxiter):
            mid = (a + b) / 2
            fa, fb, fmid = f(a), f(b), f(mid)
            table.append((i + 1, a, b, mid, fa, fb, fmid))
            if abs(fmid) < tol:
                return mid, table
            if fa * fmid < 0:
                b = mid
            else:
                a = mid
        return mid, table

    def false_position(a, b, maxiter, tol=1e-6):
        for i in range(maxiter):
            fa, fb = f(a), f(b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c)
            table.append((i + 1, a, b, c, fa, fb, fc))
            if abs(fc) < tol:
                return c, table
            if fa * fc < 0:
                b = c
            else:
                a = c
        return c, table

    def newton_raphson(a, maxiter, tol=1e-6):
        for i in range(maxiter):
            fa = f(a)
            dfa = df(a)
            if dfa == 0:
                print("Derivative is zero. Method fails.")
                return None, table
            a_new = a - fa / dfa
            table.append((i + 1, a, fa, dfa))
            if abs(a_new - a) < tol:
                return a_new, table
            a = a_new
        return a, table

    def trapezoidal_rule(a, b, n):
        h = (b - a) / n
        result = 0.5 * (f(a) + f(b))
        table.append((0, a, f(a), result))
        running_sum = result
        for i in range(1, n):
            xi = a + i * h
            fx = f(xi)
            running_sum += fx
            table.append((i, xi, fx, running_sum))
        integral = running_sum * h
        return integral, table

    def simpsons_rule(a, b, n):
        if n % 2 != 0:
            raise ValueError("Simpson's Rule requires even number of intervals.")
        h = (b - a) / n
        result = f(a) + f(b)
        table.append((0, a, f(a), 1))
        for i in range(1, n):
            xi = a + i * h
            fx = f(xi)
            coeff = 4 if i % 2 == 1 else 2
            result += coeff * fx
            table.append((i, xi, fx, coeff))
        table.append((n, b, f(b), 1))
        integral = result * h / 3
        return integral, table

    if method == "Bisection":
        return bisection(a, b, maxiter)
    elif method == "False Position":
        return false_position(a, b, maxiter)
    elif method == "Newton Raphson":
        return newton_raphson(a, maxiter)
    elif method == "Trapezoidal Rule":
        return trapezoidal_rule(a, b, maxiter)
    elif method == "Simpson's Rule":
        return simpsons_rule(a, b, maxiter)
    else:
        raise ValueError("Invalid method selected.")
