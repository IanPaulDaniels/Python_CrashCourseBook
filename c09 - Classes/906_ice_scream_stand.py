from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self):   
        super().__init__("B&J", 'Ice Cream Stand')
        self.flavors = ['strawberry', 'vainilla']

    def display_flavors(self):

        print(self.restaurant_name + "'s flavors are:")
        for flavor in self.flavors:
            print("\t- " + flavor.title())

ics = IceCreamStand()

ics.display_flavors()