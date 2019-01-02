pizza = {
    'crust': 'meduim',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You've ordered a " + pizza['crust'] +
      "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t-"+topping.title())
