import json

filename = 'Chapter10/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username)
