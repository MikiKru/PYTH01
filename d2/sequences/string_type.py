import math

s = "This is my favourite quote: \"I\'m your father!\""
print(s)
special = "\\url"
print(special)

print('abnormal\t', 'a\bnormal')
print()

symbol = 'π'
print(symbol, ord(symbol))
print(68, chr(68))

print("alaA" < "ala")
print("Ala" < "alA")
print("aaaaaaaaaa" < "B")
print("A" < "bbbbbbbbbbbbbbbbbb")
# print(math.pi)

text = ("dddddddddddd"
       "edddd" 
       "fd" 
       "gd")
print(text)

# old-style formatting
name = "Adam"
age = 40
salary = 12_222.566
print("Name: \t\t%10s\nage: \t\t%10d\nsalary: \t\t%10.2fPLN" % (name, age, salary))
print("Name: {} \nage: {}\nsalary: {} PLN".format(name, age, salary))
print(f"Name: {name} \nage: {age:20}\nsalary: {salary:20.2f} PLN")

print(101, str(bin(101)).replace('0b','').zfill(10))
print(150, str(bin(150)).replace('0b','').zfill(10))
print(900, str(bin(900)).replace('0b','').zfill(10))

text = 'Ala ma kota, a kot ma Ale'
print(text.find("kot"))
print(text.index("a"))
print(text.upper().replace(",","").split(" "))
print(text[0], text[len(text) - 1], text[-1])







