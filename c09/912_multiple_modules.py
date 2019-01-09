from users import User
from privileges import Admin, Privileges

adminInstance = Admin('J.', 'Betancourt', 32, 'el_beta')

adminInstance.describe_user()
adminInstance.privileges.show_privilages()
