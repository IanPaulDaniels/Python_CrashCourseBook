import json

numbers = [2,3,5,7,1,13]

filename = 'Chapter10/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
