# klasa - szablon
class Example:
    pass
class User:
    def __init__(self, user_id, user_login, user_password, user_status=True):         # konstruktor -> inicjalizator
        self.user_id = user_id      # self -> przypisz do atrybutu globalnego w klasie wartość podaną z argumentu
        self.user_login = user_login
        self.user_password = user_password
        self.user_status = user_status
    def print_attributes(self):
        return "user_id={}\nuser_login={}\nuser_password={}\nuser_status={}".format(self.user_id, self.user_login, self.user_password, self.user_status)

# print(User.user_id, User.user_login, User.user_password, User.user_status)
# print(User.__dict__['user_id'])

# utworzenie obiektu klasy
user1 = User(1, "mk", "mk")      # nowa instancja utworzona na podstawie konstuktora domyślnego
print(user1.user_id, user1.user_login, user1.user_password, user1.user_status)
user1.user_password = "xxx"
print(user1.print_attributes())
user1.email = "example@email.pl"
print(user1.__dict__)

user2 = User(2, "kk", "kk", False)      # nowa instancja utworzona na podstawie konstuktora domyślnego
print(user2.user_id, user2.user_login, user2.user_password, user2.user_status)
print(user2.print_attributes())

s = "abc"
print(isinstance(user1, User), isinstance(user2, User), isinstance(s, User))
print(user1.__class__)
print(s.__class__)
print(Example().__dict__)

setattr(user1, 'email',"yyy")
print(getattr(user1,'email'))