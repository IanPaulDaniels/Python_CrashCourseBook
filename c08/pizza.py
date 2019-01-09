def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("\t- " + topping.title())


make_pizza(16, 'pepperoni')
make_pizza(18, 'mushrooms', 'green peppers', 'extra cheese')
