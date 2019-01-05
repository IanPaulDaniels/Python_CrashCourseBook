import json

filename = 'Chapter10/favorate_number.json'

with open(filename) as f_obj:
    fNumber = json.load(f_obj)
    print("I know your favorate number! It's " + fNumber)
