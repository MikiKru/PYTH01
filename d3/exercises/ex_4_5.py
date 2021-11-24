from d3.exercises.ex_4_2 import get_data

data = get_data()

filter_woman = lambda p : p['plec']
data_to_csv = lambda p : "{};{};{};{}\n".format(p['imie'], p['nazwisko'], p['wiek'], p['plec'])

print(data)
print(filter_woman(data[2]))
print(data_to_csv(data[0]))





