from Matrix1 import input_matrix, add_matrices, subtract_matrices, multiply_matrices

def display_matrix(matrix, label):
    print(f"\n{label}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def test_main():
    print("Matrix Operations: Addition / Subtraction / Multiplication")
    method = input("Choose method  Addition / Subtraction / Multiplication: ").lower()

    rows_A = int(input("Enter number of rows of Matrix A: "))
    cols_A = int(input("Enter number of columns of Matrix A: "))
    A = input_matrix(rows_A, cols_A)

    rows_B = int(input("Enter number of rows of Matrix B: "))
    cols_B = int(input("Enter number of columns of Matrix B: "))
    B = input_matrix(rows_B, cols_B)

    display_matrix(A, "Matrix A")
    display_matrix(B, "Matrix B")

    if method == "addition" or method == "subtraction":
        if rows_A == rows_B and cols_A == cols_B:
            if method == "addition":
                result = add_matrices(A, B)
                display_matrix(result, "Addition (A + B)")
            else:
                result = subtract_matrices(A, B)
                display_matrix(result, "Subtraction (A - B)")
        else:
            print("Addition/Subtraction not possible: Matrices must be of same dimensions.")

    elif method == "multiplication":
        if cols_A == rows_B:
            result = multiply_matrices(A, B)
            display_matrix(result, "Multiplication (A x B)")
        else:
            print("Multiplication not possible: Columns of A must equal rows of B.")
    else:
        print("Invalid method selected.")

if __name__ == "_main_":
  test_main()

test_main()
