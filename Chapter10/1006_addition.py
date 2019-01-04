print("Give me two numbers and i'll add them!")

first_number = input("\nFirst Number: ")
second_number = input("\nSecond Number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print('NAN detected')
else:
    print(first_number, '+', second_number, '=', answer)
