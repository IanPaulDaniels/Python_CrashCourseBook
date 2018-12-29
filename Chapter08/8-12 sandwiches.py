def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("\t- " + ingredient.title())


make_sandwich('lettuce')
make_sandwich('tomato', 'american cheese')
make_sandwich('bacon', 'lettuce', 'tomato')
