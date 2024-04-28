import unittest
from population import city_country

class City(unittest.TestCase):
    """Test for 'city_functions.py'"""
    
    def test_city_country(self):
        """Do values like 'Santiago, Chile' work"""
        locations = city_country('Lagos', 'Nigeria')
        self.assertEqual(locations,'Lagos, Nigeria')
    
    def test_city_country_population(self):
        """Do values like 'Santiago, Chile - population 500000' work"""
        location = city_country('santiago', 'chile', population= 500000)
        self.assertEqual(location, 'santiago, chile - population 500000')
unittest.main()