class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")


r1 = Restaurant('atutiplen', 'seafood')
r2 = Restaurant("Bun's Burgers", 'Burger Joint')
r3 = Restaurant('Cafe 18', 'Caribbean Restaurant')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
