import unittest
from employee_details import Employee

class TestEmployee(unittest.TestCase):
    """Test for Employee class"""
    
    def setUp(self):
        """Create an instance of Employee"""
        self.my_employee =  Employee('Samuel', 'Adekoya', 40000)
    
    def test_give_default_raise(self):
        """Gives the default raise of 5000"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 45000)
    
    def test_give_custom_raise(self):
        """Gives the employee a custom raise"""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 50000)

unittest.main()