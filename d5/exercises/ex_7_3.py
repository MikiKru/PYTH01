from d5.exercises.ex_6_1.model.address import Address
from d5.exercises.ex_6_1.model.person import Person

a1 = Address("Królewska 20", '00-000', 'Warszawa')
a2 = Address("Nowa 5", '02-100', 'Wrocław')
p1 = Person("Adam","Kowalski", a1)
p2 = Person("Anna","Kowalska", a1)
p3 = Person("Jan","Nowak", a2)

print(p1)
print(p2)
print(p3)