from privileges import Admin, Privileges, User

adminInstance = Admin('J.', 'Betancourt', 32, 'el_beta')

adminInstance.describe_user()
adminInstance.privileges.show_privilages()