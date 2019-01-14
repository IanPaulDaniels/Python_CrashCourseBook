import json

filename = 'Chapter10/favorate_number.json'

fNumber = input("what is your favorate number?\n")

with open(filename, 'w') as f_obj:
    json.dump(fNumber, f_obj)