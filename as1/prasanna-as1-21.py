# Assuming matrix dimensions are compatible for multiplication (m x n) * (n x p)
matrix1 = [[int(input("Enter element ({}, {}): ".format(i, j))) for j in range(2)] for i in range(2)]
matrix2 = [[int(input("Enter element ({}, {}): ".format(i, j))) for j in range(2)] for i in range(2)]

result_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

print("Product of matrices:")
for row in result_matrix:
    print(row)
