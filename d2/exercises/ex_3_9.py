months = ("STY*","LUT","MAR","KWI*","MAJ","CZE","LIP*","SIE","WRZ","PAŹ*","LIS","GRU")

quarters = []

for index, month in enumerate(months):
    if index % 3 != 0:
        continue
    quarters.append(months[index : index + 3])

print(quarters)

# ??? - uproszczona wersja ?!