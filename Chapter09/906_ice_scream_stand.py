from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self):   
        self.flavors = ['strawberry', 'vainilla']
        self.cuisine_type = 'Ice Cream Stand'
        self.restaurant_name = ''

    def display_flavors(self):
        print(self.flavors)

