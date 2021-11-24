def check_day_number(year, month, day):
    z = year
    c = 2
    if month < 3:
        z = year - 1
        c = 0
    day_index = (int((23 * month) / 9) + day + 4 + year + int(z / 4) - int(z / 100) + int(z / 400) - c) % 7
    return day_index
def map_index_to_day(index):
    days_list = ("NDZ", "PON", "WT", "ŚR", "CZW", "PT", "SOB")
    return days_list[index]
def date_valid():
    while True:
        date_to_valid = input("podaj datę:")
        try:  # try nasłuchuje na błędy w programie i przekazuje je do except
            if date_to_valid.find("-") == 4:
                year = int(date_to_valid[0:4])
                month = int(date_to_valid[5:7])
                day = int(date_to_valid[8:])
            elif date_to_valid.find(".") == 2:
                year = int(date_to_valid[6:])
                month = int(date_to_valid[3:5])
                day = int(date_to_valid[0:2])
            day_index = check_day_number(year, month, day)
            day_name = map_index_to_day(day_index)
            print(f"day index: {day_index}")
            print(f"day name: {day_name}")
            break
        except:
            print("Błąd daty")
date_valid()

