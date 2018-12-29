from users import User

class Admin(User):
    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name,last_name,age,username)
        self.privilages = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    
    def show_privilages(self):
        full_name = self.first_name + ' ' + self.last_name

        print(full_name.title() + ' has the following privileges: ')
        for privilege in self.privilages:
            print('\t- ' + privilege.title())

new_admin = Admin('ian', 'daniels', 28, 'idaniels')

new_admin.show_privilages()