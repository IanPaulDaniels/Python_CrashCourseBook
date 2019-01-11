import unittest
from city_functions import cityCountry

class citiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = cityCountry('san juan', 'puerto rico')
        
        self.assertEqual(formatted_city, 'San Juan, Puerto Rico')

    def test_city_country_population(self):
        formatted_city = cityCountry('san juan', 'puerto rico', 250001)
        
        self.assertEqual(formatted_city, 'San Juan, Puerto Rico - Population 250001')

unittest.main()