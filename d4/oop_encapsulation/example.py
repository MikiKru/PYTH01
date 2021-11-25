class Calc:
    def __init__(self, digit : int, number : int):
        self.set_digit(digit)
        self.__number = number
    def get_number(self):
        return self.__number
    def set_number(self, number):
        print("Modyfikuje przez setter")
        self.__number = number
    def get_digit(self):
        return self.__digit
    def set_digit(self, digit : int):
        print("setter digit")
        if digit < 0:
            self.__digit = 0
        elif digit > 9:
            self.__digit = 9
        else:
            self.__digit = digit
    def __str__(self):
        return f"class = {self.__class__.__name__} digit = {self.__digit} number = {self.number}"
    number = property(get_number, set_number)
c1 = Calc(5,1)
print(c1, c1.get_digit())
c1.number = 10              # bezpośrednio
c1.set_number(9)            # przez metodę
print(c1)
c1.set_digit(5)
# c1.__digit = 3
# c1.email = 444
print(c1)
c1.set_number(c1.get_number() * 2)

