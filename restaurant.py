class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("At " + self.restaurant_name + " we serve the following cuisines:" )
        print("\t\t" + self.cuisine_type)
    
    def open_restaurant(self):
        print("Our restaurant is currently open")

