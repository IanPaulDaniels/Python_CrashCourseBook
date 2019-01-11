class User():
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        # Add attribute called login_attempts
        self.login_attempts = 0

    def describe_user(self):
        print("User Information:")
        print("\tFull Name: " + self.first_name.title() +
              " " + self.last_name.title())
        print("\tAge: " + str(self.age))
        print("\tUsername: " + self.username)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + "!")

    # Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    # Write another method called rest_login_attempts() that rests the value of login_attempts to 0
    def rest_login_attempts(self):
        self.login_attempts = 0

u1 = User('Ian', 'Daniels', 28, 'idaniels')

# call increment_login_attempts several times
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()

# Print the value of login_attempts
print(u1.login_attempts)

# Reset the value and print
u1.rest_login_attempts()
print(u1.login_attempts)
