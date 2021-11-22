count = 5

while count:
    print(count)
    count -= 1          # count = count - 1
else:
    print("koniec")


names = ["Ala", "Anna", "Michał", "Adam", "Jan"]
for index, name in enumerate(names):
    print(index, name)
else:
    print("koniec")

print(names[1])


to_find = 1
numbers = [2,3,1,4,3,2,1,5,4,3,3]

for index, number in enumerate(numbers):
    print(f"iteracja {index}")
    if number != to_find:
        continue
    print(f"znaleziono liczbę {to_find}")
    break

while True:
    decision = input("podaj wartość (q) - wyjście")
    if(decision.upper() == "Q"):
        break
    print("iteruj dalej")

    


