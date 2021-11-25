from datetime import date

class Osoba:
    def __init__(self, imie : str, nazwisko : str,  rok_urodzenia : int, plec : bool):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__plec = plec
        self.__rok_urodzenia = rok_urodzenia
    def __str__(self):
        return f"{self.__imie} {self.__nazwisko}, płeć: {self.__plec}, wiek: {self.wiek()} lat"
    def wiek(self):
        return date.today().year - self.__rok_urodzenia
    def inkrementuj_rok_urodzenia(self):
        self.__rok_urodzenia += 1
    def ustaw_imie(self, imie):
        self.__imie = imie
    def wypisz_imie(self):
        return self.__imie
    def ustaw_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko
    def wypisz_nazwisko(self):
        return self.__nazwisko
    def ustaw_plec(self, plec):
        self.__plec = plec
    def wypisz_plec(self):
        return self.__plec
    def ustaw_rok_urodzenia(self, rok_urodzenia):
        self.__rok_urodzenia = rok_urodzenia
    def wypisz_rok_urodzenia(self):
        return self.__rok_urodzenia
