from statistics import mean

p1 = {"imie": "Anna", "nazwisko": "Nowak", "wiek": 40, "plec": True}
p2 = {"imie": "Anna", "nazwisko": "Kowalska", "wiek": 30, "plec": True}
p3 = {"imie": "Jan", "nazwisko": "Nowak", "wiek": 40, "plec": False}
p4 = {"imie": "Artur", "nazwisko": "Kwiatkowski", "wiek": 50, "plec": False}
p5 = {"imie": "Ewa", "nazwisko": "Janowicz", "wiek": 21, "plec": True}

people = [p1, p2, p3, p4, p5]
# people_dict = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5}
# people_dict = zip([1, 2, 3, 4, 5], [p1, p2, p3, p4, p5])

# zwróć tylko kobiety:                                  SELECT * FROM people WHERE plec = true;
print([p for p in people if p["plec"]])

# zwróć listę mężczyzn w wieku powyżej 45 lat           SELECT * FROM people WHERE plec = false and wiek > 45
print([p for p in people if (not p["plec"] and p["wiek"] > 45)])

# zwróć śrędnią wartość wieku wszystkich kobiet         SELECT avg(wiek) FROM people WHERE plec = true;
ages = [p["wiek"] for p in people if p["plec"]]
print(mean(ages))