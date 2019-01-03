filename = 'Chapter10/guest_book.txt'

while (True):
    user_name = input('Please enter your name: ')

    if user_name == 'exit':
        break

    with open(filename, 'a') as file_object:
        file_object.write(user_name + '\n')