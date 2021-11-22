# CTRL + ALT + L    -> formatowanie kodu
# CTRL + D          -> duplikowanie linii gdzie znajduje się kursor
# CTRL + Q          -> dokumentacja
# CTRL + /          -> komentowanie
'''


Komentarz blokowy


'''
print("Hi Python")

name = 'Michał'
number = 20
numbers = [1,2,3,4,45,5,
           5,4,3]

if (number % 2 == 0):
    print("liczba parzysta")
    print("liczba parzysta")
    print("liczba parzysta ..................................."
          "ddd.....")

print(numbers)
print(1, number, name, sep=';', end="\t\t\t")
print("...", 1)

print(round(3.14546546575434534,3))

# interakcja z użytkownikiem
# name = input("Podaj imię: ")
# print("Witaj " + name)
# height = input("Podaj wzrost w metrach: ")
# print("Twój wzrost w m: " + height)
# print((float(height) * 100))
# print("Twój wzrost w cm: " + str(float(height) * 100))

x = 1
y = x
print(x, y)
# x = 'mmm'
print(x, y)

text = "Hello Python!!!"
substring = text[1:5]
print(text, substring)
print(type(x), type(text))
