from d3.exercises.ex_4_1 import date_valid

# date_valid()

# Napisz funkcję która przy wywołaniach zwraca napiemiennie wartości True i False
status = True
a = 1
def get_status():
    global status
    status = not status
    a = 2
    return status

print(status, a)
print(get_status())
print(status, a)
print(get_status())
print(status, a)
