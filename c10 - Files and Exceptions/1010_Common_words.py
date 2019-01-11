folder = 'Chapter10/'
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
word = 'alice'

for filename in filenames:
    try:
        with open(folder+filename, encoding='utf-8') as f_obj:
            f_lines = f_obj.readlines()
            line_count = 0
            for line in f_lines:
                line_count += line.lower().count(word)
            
            print(filename + ' has ' + str(line_count) + " ocurrences of the word '" + word + "'")
    except FileNotFoundError:
        pass