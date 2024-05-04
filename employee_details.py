class Employee():
    """A representation of an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Stores the details of employees """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_raise = 5000):
        """Adds a raise to the salalry of an employee"""
        self.annual_salary += salary_raise



my_employee = Employee('Samuel', 'Adekoya', 40000)
