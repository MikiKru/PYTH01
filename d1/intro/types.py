salary = 1_000_000.
print(salary)

numberBin = 0b111
numberHex = 0x21  # 0 - 9, 10 - A, 11 - B ...
print(numberBin, numberHex)

# jak int wypisać w postaci binarnej na ekranie???
# bin
numberDec = 7
print(bin(numberDec))
print(f'{numberDec:b}')

x = 2.
y = 3.
print(type(x), type(y), int(x / y))
print(type(x), type(y), x // y)

# a = 1         przypisanie
# a == 1        porównanie

p = True
q = False

print(p and q)
print(p or q)
print(not q)

num = 7

print(num, bin(num << 2), bin(num >> 2))
print(num, num << 2, num >> 2)

is_true_or_false = "njksdnaj"
print(type(bool(is_true_or_false)), type(True))

