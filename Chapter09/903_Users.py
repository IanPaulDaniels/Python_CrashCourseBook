class User():
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username

    def describe_user(self):
        print("User Information:")
        print("\tFull Name: " + self.first_name.title() +
              " " + self.last_name.title())
        print("\tAge: " + str(self.age))
        print("\tUsername: " + self.username)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + "!")


u1 = User('Ian', 'Daniels', 28, 'idaniels')
u2 = User('Elizabeth', 'Gomez', 27, 'egomez')

u1.greet_user()
u1.describe_user()

u2.greet_user()
u2.describe_user()
