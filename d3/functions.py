def welcome():              # nie przyjmuje argumentów i nie zwraca wartości
    print("Hello")

def welcome_me(name):       # przyjmuje argument i nie zwraca wartości
    print(f"Hello {name}")

def one():                  # nie przyjmuje argumentów i zwraca wartość
    return 1

def addition(num1, num2):   # przyjmuje arghumenty i zwraca wartość
    return num1 + num2

def subtraction(num1, num2):   # przyjmuje arghumenty i zwraca wartość
    return num1 - num2

def divsion(num1, num2):
    return num1, num2, num1 / num2

def f(x, a=1, b=2):             # parametry obowiązkowe muszą być pierwsze
    print(x, a, b)

def fun(element, *arg):
    lista = [*arg]
    lista.append(element)
    print(lista)

def fun2(element, l = []):
    l.append(element)
    print(l)

def fun3(x, **kwargs):
    print(x)
    for key, value in kwargs.items():
        print(key, value)
