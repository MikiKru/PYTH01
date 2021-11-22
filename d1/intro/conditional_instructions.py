number = -33
isPositive = False

if(number > 0):
    isPositive = True

if(number == 0):
    print("liczba zero")
elif(number % 2 == 0 and isPositive):
    print("liczba parzysta dodatnia")
elif(number % 2 == 0 and not isPositive):
    print("liczba parzysta ujemna")
elif (number % 2 == 1 and isPositive):
    print("liczba nieparzysta dodatnia")
elif (number % 2 == 1 and not isPositive):
    print("liczba nieparzysta ujemna")

# if(number == 0):
#     print("liczba zero")
# elif(number % 2 == 0):
#     if(number > 0):
#         print("liczba parzysta dodatnia")
#     else:
#         print("liczba parzysta ujemna")
# else:
#     if (number > 0):
#         print("liczba nieparzysta dodatnia")
#     else:
#         print("liczba nieparzysta ujemna")
print("koniec")


name = "Anna"
print("kobieta".upper() if name[len(name) - 1].upper() == "A" else "mężczyzna".upper())

