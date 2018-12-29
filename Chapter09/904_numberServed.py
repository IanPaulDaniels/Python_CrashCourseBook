class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Add an attribute called number_served with a default value of 0
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant's name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")
    
    # Add a method called set_number_served() that lets you set the number of customers that have been served.
    def set_number_served(self, number_served):
        self.number_served = number_served

    # Add a method called increment_number_served() that lets you increment the number of customers who've been served.
    def increment_number_served(self, number_served):
        self.number_served += number_served

# Create an instance called restaurant from this class.
restaurant = Restaurant('atutiplen', 'seafood')

# Print the number of customers the restaurant has served and then change this value and print it again.
print(restaurant.number_served)
restaurant.number_served = 4
print(restaurant.number_served)

# Call set_number_served() with a new number nad print the value again.
restaurant.set_number_served(45)
print(restaurant.number_served)

# Call the increment_number_served() method with any number you like
restaurant.increment_number_served(150)
print(restaurant.number_served)
