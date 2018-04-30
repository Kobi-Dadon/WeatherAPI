import requests
from flask import json
from api.settings import W_API_ID, W_API_URL, W_API_UNITS


class WeatherController(object):

    def __init__(self, city):
        self.city = city

    def get_info(self):
        """
        get all information needed in a convenient format
        :return: a dictionary contains all relevant information
        """
        params = {
            'q': self.city,
            'appid': W_API_ID,
            'units': W_API_UNITS
        }
        url = W_API_URL + '/data/2.5/weather'
        results = requests.get(url, params)
        return self.__info_encoder(json.loads(results.text)) if results.status_code == 200 else None

    def __info_encoder(self, res):
        """
        encode to convenient format
        :param res: raw results dictionary from the API call
        :return: a dictionary with information
        """
        info = {
            'name': res['name'],
            'main': res['weather'][0]['main'],
            'main_descr': res['weather'][0]['description'],
            'icon': W_API_URL + '/img/w/{}.png'.format(res['weather'][0]['icon']),
            'temp': res['main']['temp'],
            'max_t': res['main']['temp_max'],
            'min_t': res['main']['temp_min'],
            'humid': res['main']['humidity'],
        }
        return info
