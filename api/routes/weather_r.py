from api.app import get_app
from flask_restplus import Resource, abort
from api.controllers.weather_c import WeatherController
from api.namespaces import ns_weather

app = get_app()


@ns_weather.route("/<city>")
class Weather(Resource):

    @app.api.doc(
        responses={
            200: 'Success',
            404: 'Not found'
        },
        description='Get weather information by city'
    )
    def get(self, city):
        """
        GET call for information by city
        :param city: city name
        :return: a dictionary with all information
        """
        info = WeatherController(city).get_info()
        if not info:
            abort(404, 'No information was found for this destination.')
        return info, 200
