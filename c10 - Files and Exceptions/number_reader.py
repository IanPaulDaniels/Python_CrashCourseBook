import json

filename = 'Chapter10/numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)