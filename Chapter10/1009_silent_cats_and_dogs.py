folder = 'Chapter10/'
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(folder+filename) as f_obj:
            contents = f_obj.read()
            print('Contents of file: ' + filename)
            print(contents)
    except FileNotFoundError:
        pass