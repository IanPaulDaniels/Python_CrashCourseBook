def count_words(filename):
    """Count the proximate number of words in the file"""

    folder = 'Chapter10/'

    try:
        with open(folder + filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry. The file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
