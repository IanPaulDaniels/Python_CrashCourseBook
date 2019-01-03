filename = 'Chapter10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

docString = ''
for line in lines:
    docString += line

print(docString)

print(docString.replace('Python', 'C'))