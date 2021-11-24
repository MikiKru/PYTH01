from statistics import mean

from d3.exercises.ex_4_2 import get_data

numbers = [1,2,3,4,3,2,2,1,3,4,4,2,2,3,7,8,9]
print(mean(numbers))

def get_data_upper_avg(number):
    return number >= mean(numbers)

result = filter(get_data_upper_avg, numbers)
print(result)
print(*result)

cyfry = range(10)
print(*cyfry)
f = filter(None, cyfry)
print(*f)

ids = range(1,10)
def get_id_repr(id):
    # return "id=" + str(id)
    return f"'id'={id}"
m = map(get_id_repr, ids)
print(*m)


data = get_data()
def order_by_lastname(p):
    return p['nazwisko'], p['imie']
# print(sorted(data, key=order_by_lastname, reverse=True))
print(sorted(data, key=order_by_lastname, reverse=True))



