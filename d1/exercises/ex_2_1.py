from random import randint, choices

rnd_number = randint(1, 6)
print("Wyrzucono: " + str(rnd_number))

# statystyki rzutów kostką
numbers = [1,2,3,4,5,6]
stats = choices(numbers, k = 100)
print(stats)
