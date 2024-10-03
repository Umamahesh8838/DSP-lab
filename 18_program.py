# Matrix addition using nested lists
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print("Result of matrix addition:")
for row in result_matrix:
    print(row)
