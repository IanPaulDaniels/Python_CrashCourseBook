unconfirmed_users = ['ana', 'daryll', 'candance']
current_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())

    current_users.append(current_user)

for user in current_users:
    print(user.title())
