class Example:
    def __init__(self):
        print("Konstruktor klasy Example")
class Software(Example):
    def __init__(self, name, language):
        super().__init__()
        print("Konstruktor klasy Software")
        self.name = name
        self.language = language
    def __str__(self):
        return f"name = {self.name} language = {self.language}"

class Course(Software):
    def __init__(self, name, language, price):
        super().__init__(name, language)      # musi byćpierwszą linią metody
        self.price = price
        print("Konstruktor klasy Course")
    def __str__(self):
        return f"{super().__str__()} price = {self.price}"

s = Software("System X", "Python")
c = Course("PYTH01", "Python", 2000.)

print(s)
print(c)
print(s.__dict__)
print(c.__dict__)

print(Software.__bases__)
print(Course.__bases__)



