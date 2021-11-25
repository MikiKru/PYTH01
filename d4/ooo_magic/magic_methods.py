class Auto:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price
    def __str__(self):
        return f"{self.model} {self.brand} {self.price}"
    def __eq__(self, other):
        return (self.model == other.model) and (self.brand == other.brand)
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        print("le", len(self.model), len(other.model))
        return len(self.model) <= len(other.model)


a1 = Auto("VW", "Passat", 150_000)
a2 = Auto("Audiiiiiiii", "A6", 250_000)
a3 = Auto("Audi", "A6", 260_000)
a4 = Auto("Mercedes", "GLE", 460_000)

print(a1 == a2)
print(a1.__eq__(a2))
print(a2 == a3)
print(a2 > a3)
print(a4 > a3)
print(a4 <= a2)


