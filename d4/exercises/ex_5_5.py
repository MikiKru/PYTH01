from d3.exercises.ex_4_2 import get_data
# 1 - porównanie na podstawie operatorów - osoba reprezentowana przez słownik
people = get_data()

# 2 - przeciążanie operatorów - reprezentowane na podstawie własnego obiektu
class Person:
    def __init__(self, name, last_name, age, gender):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def __eq__(self, other):
        if self.last_name != other.last_name:
            return False
        elif self.name == other.name:
            return True
        else:
            return False

p1 = Person("Adam","Kowalski", 30, True)
p2 = Person("Adam","Nowak", 30, True)
p3 = Person("Jan","Kowalski", 30, True)

print(p1 == p1)
print(p1 == p2)
print(p1 == p3)




