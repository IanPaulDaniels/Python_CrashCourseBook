current_users = ['idaniels', 'admin', 'jlindsey', 'acarmichael', 'mdaniels']
new_users = ['jlindsey', 'mdaniels', 'mllanos', 'cdaniels']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ' is already taken, please enter a new username')
    else:
        print(new_user + ' is available')
