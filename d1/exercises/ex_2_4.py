from math import factorial

k = 6
n = 49

chance = factorial(n)/(factorial(k) * factorial(n - k))

print(f"Szanse rozbicia banku: {1 / chance}")