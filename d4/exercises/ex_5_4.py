class Employee:
    def __init__(self, name, last_name, salary):
        self.__name = name
        self.__last_name = last_name
        self.__salary = salary
    def employee_str(self):
        return f"{self.__name}, {self.__last_name}, {self.__salary}"
    def __str__(self):
        return f"[{self.__class__.__name__}]: {self.employee_str()}"
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

# kontroler -> implementuje metody do obsługi klasy modelu
class Manager(Employee):
    def __init__(self, name, last_name, salary, employees=[]):
        super().__init__(name, last_name, salary)
        self.__emploees = employees
    def __str__(self):
        return f"[{self.__class__.__name__}] {super().employee_str()} zaspół: {[e.__str__() for e in self.__emploees]}"
        # return f"[{self.__class__.__name__}] {super().employee_str()} zaspół: {self.__emploees}"
    def add_employee(self, employee):
        self.__emploees.append(employee)
    def remove_employee_by_index(self, index):
        try:
            self.__emploees.remove(self.__emploees[index])
        except:
            print("Błędny index!")
    def sort_employees_by_salary(self, direction):
        i = 0                                   # max n - 1 iteracji
        j = 0
        while i < len(self.__emploees):
            while j < len(self.__emploees) - 1:
                if direction:
                    if (self.__emploees[j].get_salary() > self.__emploees[j + 1].get_salary()):
                        e = self.__emploees[j]
                        self.__emploees[j] = self.__emploees[j + 1]
                        self.__emploees[j + 1] = e
                    j += 1
                else:
                    if (self.__emploees[j].get_salary() < self.__emploees[j + 1].get_salary()):
                        e = self.__emploees[j]
                        self.__emploees[j] = self.__emploees[j + 1]
                        self.__emploees[j + 1] = e
                    j += 1
            i += 1


e1 = Employee("Adam", "Kowalski", 16_000.50)
e2 = Employee("Janusz", "Nowak", 10_000.50)
e3 = Employee("Anna", "Kowalska", 12_000.50)
e4 = Employee("Ala", "Kowalska", 12_000.50)
m = Manager("Jan","Nowak", 24_000)
m.add_employee(e1)
m.add_employee(e2)
m.add_employee(e3)
m.add_employee(e4)
# m.remove_employee_by_index(1)
m.sort_employees_by_salary(False)
print(m)
