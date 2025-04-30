from Method import bisection, false_position, newton_raphson

def test_main():
    print ( " Starting the program ")
    func_str = input("Enter the function (e.g., tan(x) - x): ")
    method = input("Choose method (bisection/false_position/newton_raphson): ").lower()

    if method == "bisection" or method == "false_position":
        a = float(input("Enter the lower guess (a): "))
        b = float(input("Enter the upper guess (b): "))

        if method == "bisection":
            root = bisection(func_str, a, b, verbose=True)
        else:
            root = false_position(func_str, a, b, verbose=True)

    elif method == "newton_raphson":
        x0 = float(input("Enter the initial guess (x0): "))
        root = newton_raphson(func_str, x0, verbose=True)

    else:
        print("Invalid method selected!")
        return

    print(f"\nEstimated root using {method} method is: {root}")

if __name__ == "_main_":
    test_main()

test_main()
