from city_functions import formatted_city_country
import unittest

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string=formatted_city_country('london','england')
        self.assertEqual(formatted_string,'London,England')

    def test_city_country_population(self):
        formatted_string=formatted_city_country('santiago','chile',5000000)
        self.assertEqual(formatted_string,'Santiago,Chile - population 5000000')

unittest.main()

