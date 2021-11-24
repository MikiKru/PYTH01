from d3.exercises.ex_4_2 import get_data

data = get_data()


# funkcja zwracająca osoby płci żeńskiej
def filter_woman(p):
    return p['plec']

print(*filter(filter_woman, data))

# funkcja która zwróci każdy rekrod w formacie csv ;
def data_to_csv(p):
    # p : dict            # typowanie statyczne
    # values = p.values()
    # print(*values)
    # return
    return "{};{};{};{}\n".format(p['imie'], p['nazwisko'], p['wiek'], p['plec'])
print(*map(data_to_csv, data))