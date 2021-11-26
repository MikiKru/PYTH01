def get_positive_value(value):
    if(value < 0):
        return 0
    return value

class Person:
    def __init__(self, name, last_name, age, gender):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def __eq__(self, other):
        if self.last_name != other.last_name:
            return False
        elif self.name == other.name:
            return True
        else:
            return False

a = 1