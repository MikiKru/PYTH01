class Employee:
    def __init__(self, name, last_name, salary):
        self.__name = name
        self.__last_name = last_name
        self.__salary = salary
    def __str__(self):
        return f"[{self.__class__.__name__}]: {self.__name}, {self.__last_name}, {self.__salary}"
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_last_name(self):
        return self.__last_name
    def __set_last_name(self, last_name):
        self.__last_name = last_name
    def get_salary(self):
        return self.__salary
    def __set_name(self, salary):
        self.__salary = salary

e = Employee("Adam", "Kowalski", 10_000.50)
print(e)
