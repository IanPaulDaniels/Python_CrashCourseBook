filename = 'Chapter10/learning_python.txt'

with open(filename) as file_object:
    ## read entire object
    # print(file_object.read()) 

    ## Read line by line
    # lines = file_object.readlines()
    # for line in lines:
    #     print(line)

    ## Read by storing data in string variable
    lines = file_object.readlines()

docString = ''
for line in lines:
    docString += line

print(docString)

