import unittest
from api.app import get_app
from api.routes.weather_r import Weather


class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.app = get_app().test_client()

    def test_valid_name(self):
        response = self.app.get('/weather/Austin')
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        response = self.app.get('/weather/Hogwarts')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
