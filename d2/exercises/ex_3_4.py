# 1. losowanie 6 spośród 49 liczb naturalnych
# 2. ocena szans na wyganie
from random import randint

# algorytm obliczjący n! 4! = 4 * 3 * 2
def my_factorial(n):
    result = 1
    for num in range(2, n + 1):
        result *= num
    return result

choices = set()
while len(choices) < 6:
    choices.add(randint(1, 50))
    # if choice not in choices:
    #     choices.append(choice)

print(list(choices)[0], choices)
n = 49
k = 6
chance = my_factorial(n)/(my_factorial(k) * my_factorial(n - k))
# print(f"Szanse rozbicia banku: {1 / chance}")
chance_prob = 1 / chance
print(f"Szanse rozbicia banku: {chance_prob:.12f}")