class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("At " + self.restaurant_name + " we serve the following cuisines:" )
        print("\t\t" + self.cuisine_type)
    
    def open_restaurant(self):
        print("Our restaurant is currently open")



class  IceCreamStand(Restaurant):
    """ An ice cream class that inherits from the restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialze the ice cream stand attributes and also inherit attributes from the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate', 'Strawberry']
    
    def display_flavours(self):
        """ Displays the flavours available"""
        message = 'These are the available flavours:'
        print(message)
        for flavour in self.flavours:
            print(flavour)


my_stand = IceCreamStand('Shijoki', 'Japan Cuisine')
my_stand.display_flavours()