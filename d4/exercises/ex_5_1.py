from datetime import date

class Osoba:
    def __init__(self, imie : str, nazwisko : str,  rok_urodzenia : int, plec : bool):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia
    def __str__(self):
        return f"{self.imie} {self.nazwisko}, płeć: {self.plec}, wiek: {self.wiek()} lat"
    def wiek(self):
        return date.today().year - self.rok_urodzenia
    def inkrementuj_rok_urodzenia(self):
        self.rok_urodzenia += 1
# osoba1 = Osoba("Jan", "Kowalski", 1990,True)
# print(osoba1.__str__())
# osoba1.inkrementuj_rok_urodzenia()
# print(osoba1)