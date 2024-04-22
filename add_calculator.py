status = True

while status:
        """ A function to add two numbers """
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Please enter a second number: "))
        
        except(TypeError, ValueError):
            message = "Please enter a number"
            print(message)
        
        else:
            result = num_1 + num_2
            print(result)
