import unittest
from city_functions import cityCountry

class citiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = cityCountry('san juan', 'puerto rico')
        
        self.assertEqual(formatted_city, 'San Juan, Puerto Rico')

unittest.main()