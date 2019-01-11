available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print('Adding ' + requested_topping.title() + '.')
        else:
            print("Sorry, we're out of " + requested_topping)

    print('\nFinished making the pizza!')
else:
    print('Are you sure you want an empty pizza?')
