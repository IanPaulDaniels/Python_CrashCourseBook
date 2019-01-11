age = 12
price = 0

if age < 4:  # Kids are free!
    price = 0
elif age < 18:  # Teens
    price = 5
elif age < 65:  # Senior Discount
    price = 10
else:
    price = 5

print('Your admision cost is $' + str(price) + '.')
