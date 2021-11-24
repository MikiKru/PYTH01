matrix_one = []
dim = 4

for row_index in range(dim):
    row = []
    for col_index in range(dim):
        if col_index == row_index:
            row.append(1)
        else:
            row.append(0)
    matrix_one.append(row)
print(matrix_one)
# matrix_one_le = [[1 if row == column else 0 for column in range(dim)] for row in range(dim)]
matrix_one_le = [[int(row == column) for column in range(dim)] for row in range(dim)]
print(matrix_one_le)

