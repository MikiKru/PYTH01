from datetime import date

class NoValueError(Exception):
    def __init__(self):
        print("Zgłoszono wyjątek " + self.__class__.__name__)

class BirthDateError(Exception):
    def __init__(self):
        print("Zgłoszono wyjątek " + self.__class__.__name__)

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
    def __ustaw_imie(self, imie):
        self.__imie = imie
    def __wypisz_imie(self):
        return self.__imie
    def __ustaw_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko
    def __wypisz_nazwisko(self):
        return self.__nazwisko
    def __ustaw_plec(self, plec):
        self.__plec = plec
    def __wypisz_plec(self):
        return self.__plec
    def __ustaw_rok_urodzenia(self, rok_urodzenia):
        self.__rok_urodzenia = rok_urodzenia
    def __wypisz_rok_urodzenia(self):
        return self.__rok_urodzenia
    imie = property(__wypisz_imie, __ustaw_imie)
    naziwsko = property(__wypisz_nazwisko, __ustaw_nazwisko)
    plec = property(__wypisz_plec, __ustaw_plec)
    rok_urodzenia = property(__wypisz_rok_urodzenia, __ustaw_rok_urodzenia)

def valid_data():
    try:
        name = input("podaj imie")
        last_name = input("podaj nazwisko")
        rok_urodzenia = int(input("podaj rok urodzenia"))
        gender = input("podaj płeć (M/K)")
        if name == "" or last_name == "":
            raise NoValueError
        if gender == "M":
            gender = True
        elif gender == "K":
            gender = False
        else:
            raise NameError
        if rok_urodzenia > date.today().year:
            raise BirthDateError
        o1 = Osoba(name,last_name, rok_urodzenia, gender)
        print(o1)

    except NoValueError as ar:
        print(ar)
        print("imię i nazwisko nie może być puste")
    except NameError as ne:
        print(ne)
        print("błędny wydór płci")
    except BirthDateError as bde:
        print(bde)
        print("błędna data urodzenia - zbyt duża wartość roku urodzenia")
    except (TypeError, ValueError) as te:
        print(te)
        print("błędny wiek - nie da się skonwertować na liczbę")
    else:
        print("utworzono obiekt")

valid_data()
print("dalej działam!!!")