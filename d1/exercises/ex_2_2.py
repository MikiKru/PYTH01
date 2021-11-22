"""
Rok jest przestępny, jeśli jest wielokrotnością 4,
z wykluczeniem lat będących wielokrotnościami 100,
chyba, że są wielokrotnościami 400 (te są przestępne)
"""

year = int(input("Wprowadź rok"))
is_leap_year = year % 400 == 0 or year % 100 != 0 and year % 4 == 0

print(f"Czy rok {year} jest przestępny? {is_leap_year}")