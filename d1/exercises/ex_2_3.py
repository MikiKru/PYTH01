value = float(input("podaj wartość konta [PLN]"))
time = int(input("podaj okres lokaty (ilość lat)"))
percent = float(input("podaj oprocentowanie [%]"))

current_status = round((value * (1 + percent/100) ** time),2)

print(f"Stan konta po upłynięciu okresu lokaty: {current_status} PLN")