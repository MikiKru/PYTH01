from d5.exercises.ex_6_1.model.address import Address
from d5.exercises.ex_6_1.model.person import Person

a1 = Address("Królewska 20", '00-000', 'Warszawa')
a2 = Address("Nowa 5", '02-100', 'Wrocław')
p1 = Person("Adam","Kowalski", a1)
p2 = Person("Anna","Kowalska", a1)
p3 = Person("Jan","Nowak", a2)

people = [p1, p2, p3]

def write_people_to_book(people):
    with open("contact_book.txt", mode='w', encoding="utf-8") as f:
        for person in people:
            f.write(person.to_csv()+"\n")
    print("Zapisano do pliku")

def read_pople_from_book():
    temp_people = []
    with open("contact_book.txt", mode='r', encoding="utf-8") as f:
        for person in f.readlines():
            line = person.split(sep=";")
            a = Address(line[2], line[3], line[4])
            p = Person(line[0], line[1], a)
            temp_people.append(p)
    return temp_people

write_people_to_book(people)
for p in read_pople_from_book():
    print(p, end="")
