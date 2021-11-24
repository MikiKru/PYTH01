months = ("STY*","LUT","MAR","KWI*","MAJ","CZE","LIP*","SIE","WRZ","PAŹ*","LIS","GRU")

quarters = []

for index, month in enumerate(months):
    if index % 3 != 0:
        continue
    quarters.append(months[index : index + 3])

# print(quarters)

quarters = [[month for index, month in enumerate(months) if q_index == index // 3] for q_index in range(4)]
print(quarters)

