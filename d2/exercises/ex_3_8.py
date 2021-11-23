months = ("STY*","LUT","MAR","KWI*","MAJ","CZE","LIP*","SIE","WRZ","PAŹ*","LIS","GRU")

print(months[::3])
print("".join(month+", " for month in months if not months.index(month)%3))