import json

filename = 'Chapter10/favorate_number2.json'

try:
    with open(filename) as f_obj:
        fNumber = json.load(f_obj)
except FileNotFoundError:
    fNumber = input("what is your favorate number?\n")
    with open(filename, 'w') as f_obj:
        json.dump(fNumber, f_obj)
else:
    print("I know your favorate number! It's " + fNumber)
