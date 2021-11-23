year = int(input("podaj rok"))
count = 0
day = 13

for month in range(1,13):
    z = year
    c = 2
    if (month < 3):
        z = year - 1
        c = 0
    if ((((23 * month) // 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7) == 5:
        count += 1

print(f"W roku {year} występuje {count} piątków 13-tego")