class Person:
    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address
    def __str__(self):
        return f"{self.name} {self.last_name} {self.address}"
    def address_to_csv(self):
        return f"{self.address.street};{self.address.postal_code};{self.address.city}"
    def to_csv(self):
        return f"{self.name};{self.last_name};{self.address_to_csv()}"
