elements1 = range(10)
elements2 = range(10, 50)
elements3 = range(10, 50, 2)
print(*elements1)
print(*elements2)
print(*elements3)

for elem in range(100):
    if(elem % 2 == 0):
        print(elem, end=" ")
print()