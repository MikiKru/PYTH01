# Napisz program za pomocą pętli wykonujący operację x^y
# x,y - liczby całkowite dodatnie
# 2 ^ 3 = 8
# 2*2*2

x = int(input("podaj podstawę potęgi"))
y = int(input("podaj wykłądnik potęgi"))
temp = y
result = 1

while (temp):
    result *= x         # result = result * x
    temp -= 1

print(f"{x} ^ {y} = {result}")

result = 1
for element in range(y):
    result *= x

print(f"{x} ^ {y} = {result}")
