def get_formatted_name(first_name, last_name, middle_name=''):
    """Return the full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()


def greet_user(username):
    """Display a sample greeting."""
    print("Hello, " + username.title() + "!")


# This is an infinite loop!
while True:
    print("\nPlease tell me your name: " +
          "\n(enter q anytime to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name)
