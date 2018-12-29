magicians = ['morell', 'maraver', 'daniels']
great_magicians = []


def show_magicians(magicians):
    print('Magicians:')
    for magician in magicians:
        print('\t- ' + magician.title())


def make_great(magicians):

    while magicians:
        great_magicians.append('the great ' + magicians.pop())


show_magicians(magicians)

make_great(magicians[:])

show_magicians(great_magicians)
