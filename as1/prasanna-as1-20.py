matrix1 = [[int(input("Enter element ({}, {}): ".format(i, j))) for j in range(2)] for i in range(2)]
matrix2 = [[int(input("Enter element ({}, {}): ".format(i, j))) for j in range(2)] for i in range(2)]

result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

print("Sum of matrices:")
for row in result_matrix:
    print(row)
