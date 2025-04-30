def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1} (space-separated): ").split()))
        if len(row) != cols:
            raise ValueError("Incorrect number of columns entered.")
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(sum_product)
        result.append(row)
    return result