import unittest
from city_functions import city_country

class City(unittest.TestCase):
    """Test for 'city_functions.py'"""
    
    def test_(self):
        """Do values like 'Santiago, Chile' work"""
        locations = city_country('Lagos', 'Nigeria')
        self.assertEqual(locations,'Lagos, Nigeria')

unittest.main()