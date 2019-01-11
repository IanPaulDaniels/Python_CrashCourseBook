import json


def greet_user():
    """Greet user by name"""
    username = get_stored_username()

    if username:
        correctUser = input("Is '" + username + "' the correct username? (y/n)")
        if correctUser.lower() == 'y':
            print("Welcome back, " + username)
        elif correctUser.lower() == 'n':
            username = get_new_username()
            print("we'll remember your name next time, " + username + "!")
    else:
        username = get_new_username()
        print("we'll remember your name next time, " + username + "!")


def get_stored_username():
    """Get stored username if available"""
    filename = 'Chapter10/username.json'
    try:
         with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("what is your name? ")
    filename = 'Chapter10/username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


greet_user()
