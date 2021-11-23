matrix = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

print(matrix)

for row in matrix:
    for element in row:
        print(f"{element:2d}", end=" ")
    print()



