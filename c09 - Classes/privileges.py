from users import User

class Admin(User):
    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privilages = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    
    def show_privilages(self):
        for privilege in self.privilages:
            print('- ' + privilege.title())

new_admin = Admin('ian', 'daniels', 28, 'idaniels')

new_admin.privileges.show_privilages()
