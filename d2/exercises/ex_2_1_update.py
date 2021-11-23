from random import randint, choices
# sprawdź ile razy występuje każda wartość od 1 do 6

rnd_number = randint(1, 6)
print("Wyrzucono: " + str(rnd_number))

# statystyki rzutów kostką
numbers = [1,2,3,4,5,6]
stats = choices(numbers, k = 100)
print(stats)

counts = []
for num in numbers:
    counts.append(stats.count(num)/100)

print(counts)