class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self, number_served):
        self.number_served += number_served
    
    def describe_restaurant(self):
        print("At " + self.restaurant_name + " we serve the following cuisines:" )
        print("\t\t" + self.cuisine_type)
    
    def open_restaurant(self):
        print("Our restaurant is currently open")
    


restaurant = Restaurant('Shijoki', 'Japan Cuisine')
print(restaurant.number_served)
restaurant.set_number_served(40)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.number_served)