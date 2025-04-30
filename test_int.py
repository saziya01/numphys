import pytest
def test_main():
    import intmethod

    print("Choose a method:")
    print("1. Trapezoidal Rule")
    print("2. Simpson's Rule")

    choice = int(input("Enter your choice (1 or 2): "))

    eq_str = input("Enter equation in terms of x (e.g., 1/(1+x)): ")
    f = lambda x: eval(eq_str)  # Be cautious with eval!

    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))

    if choice == 1:
        h = float(input("Enter the step size (h) for Trapezoidal Rule: "))
        result = intmethod.trapezoidal_integration(f, a, b, h)
        print(f"Result of integration using Trapezoidal Rule from {a} to {b} is: {result}")

    elif choice == 2:
        n = int(input("Enter the number of intervals (n, must be even) for Simpson's Rule: "))
        result = intmethod.simpsons_rule(f, a, b, n)
        print(f"Result of integration using Simpson's Rule from {a} to {b} is: {result}")

    else:
        print("Invalid choice. Please select 1 or 2.")

test_main()
