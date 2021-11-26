from d5.exercises.ex_6_1.model.address import Address
from d5.exercises.ex_6_1.model.person import Person

if __name__ == '__main__':
    a1 = Address("Królewska","00-000","Warszawa")
    p1 = Person("Adam","Kowalski",a1)

    print(p1)