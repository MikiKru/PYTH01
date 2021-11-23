names = ['Ala','Adam','Ewa']
various_elements = (1, 3.14, 'A', names, (1,2,3))

print(names)
print(various_elements)
# various_elements[0] = 5 - zabronione
names.append("Michał")
print(various_elements)
print(various_elements[4][1])
