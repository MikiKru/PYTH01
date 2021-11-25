from datetime import date
# Klasa modelu - determinuje strukture danych
# 1. prywatne pola
# 2. publiczne metody dostępowe
# 3. konstruktor -> nie ma przeciążania
# 4. str -> interfejs

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
    @property
    def imie(self):
        return self.__imie
    @property
    def nazwisko(self):
        return self.__nazwisko
    @property
    def plec(self):
        return self.__plec
    @property
    def rok_urodzenia(self):
        return self.__rok_urodzenia
    @imie.setter
    def imie(self, imie):
        self.__imie = imie
    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko
    @plec.setter
    def plec(self, plec):
        print("plec setter")
        self.__plec = plec
    @rok_urodzenia.setter
    def rok_urodzenia(self, rok_urodzenia):
        print("getter rok urodzenia")
        self.__rok_urodzenia = rok_urodzenia


o = Osoba("X","X",2000, True)
print(o)
o.plec = False
o.rok_urodzenia += 5
print(o.rok_urodzenia)
print(o)
print(Osoba.__bases__)