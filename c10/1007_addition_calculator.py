print("Give me two numbers and i'll add them!")

while True:
    first_number = input("\nFirst Number: ")
    second_number = input("Second Number: ")

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('NAN detected')
        print('Please enter other values')
    else:
        if(int(second_number) < 0):
            second_number = '(' + second_number + ')'
        print(first_number, '+', second_number, '=', answer)
