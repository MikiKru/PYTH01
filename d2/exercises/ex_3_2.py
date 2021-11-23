# Dozwolone opcje wprowadzania daty
# YYYY-MM-dd
# dd.MM.YYYY

while True:
    date = input("Wprowadź datę w jednym z formatów: YYYY-MM-dd lub dd.MM.YYYY")
    if '.' in date:
        day, month, year = date.split(".")
    else:
        year, month, day = date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    if (year < 0):
        print("błędny rok")
        continue
    if (month < 1 or month > 12):
        print("błędny miesiąc")
        continue
    if (day < 1 or day > 31):
        print("błędny dzień")
        continue
    z = year
    c = 2
    if (month < 3):
        z = year - 1
        c = 0
    day_name_index = (((23 * month) // 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7
    print(day_name_index)
    break
