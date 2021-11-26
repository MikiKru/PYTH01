def start():
    while True:
        year = int(input("podaj rok"))
        month = int(input("podaj miesiąc"))
        day = int(input("podaj dzień"))

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

# from datetime import datetime
# import calendar
#
# time_str = input('Enter a date in YYYY-MM-DD format')
# my_date = datetime.strptime(time_str, "%Y-%m-%d")
#
# print(calendar.day_name[my_date.weekday()])
