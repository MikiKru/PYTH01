from statistics import mean


def get_data():
    p1 = {"imie": "Anna", "nazwisko": "Nowak", "wiek": 40, "plec": True}
    p2 = {"imie": "Anna", "nazwisko": "Kowalska", "wiek": 30, "plec": True}
    p3 = {"imie": "Jan", "nazwisko": "Nowak", "wiek": 40, "plec": False}
    p4 = {"imie": "Artur", "nazwisko": "Kwiatkowski", "wiek": 50, "plec": False}
    p5 = {"imie": "Ewa", "nazwisko": "Janowicz", "wiek": 21, "plec": True}
    return p1, p2, p3, p4, p5


# zwróć tylko kobiety:                                  SELECT * FROM people WHERE plec = true;
def get_people_by_gender(people, gender=True):
    return [p for p in people if p["plec"] == gender]

# zwróć listę mężczyzn w wieku powyżej 45 lat           SELECT * FROM people WHERE plec = false and wiek > 45
def get_people_by_gender_and_age(people, gender=False, age=45):
    return [p for p in people if (not p["plec"] and p["wiek"] > 45)]

# zwróć śrędnią wartość wieku wszystkich kobiet         SELECT avg(wiek) FROM people WHERE plec = true;
def get_age_avg_by_gender(people, gender=True):
    ages = [p["wiek"] for p in people if p["plec"]]
    return mean(ages)


people = get_data()
print(get_people_by_gender(people, gender=False))
print(get_people_by_gender_and_age(people))
result = get_age_avg_by_gender(people)
print(round(result, 1))
