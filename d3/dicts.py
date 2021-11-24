# klucze muszą być unikatowe
arabic_to_roman_conv = {0: "0", 1: "I", 2: "II", 3: "III"}
roman_to_arabic_conv = {"0": 0, "I": 1, "II": 2, "III": 3}
print(arabic_to_roman_conv[3])
print(roman_to_arabic_conv["I"])
arabic_to_roman_conv[4] = "IV"
arabic_to_roman_conv.update({3: "XXX", 4: "IV", 5: "V", 6: "VI"})
print(arabic_to_roman_conv)

en2pl = {'apple': 'jabłko', 'pear': 'gruszka','plum': 'śliwka'}
print(en2pl)
print(en2pl.items())

for key, value in en2pl.items():
    print(key, value)

for key in en2pl.keys():
    print(key, en2pl[key])

copy_en2pl = en2pl.copy()       # kopia płytka
copy_en2pl2 = en2pl             # kopia głęboka
en2pl["x"] = "y"
print(en2pl, copy_en2pl, copy_en2pl2)

l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
l1.append("X")
print(l1, l2, l3)
