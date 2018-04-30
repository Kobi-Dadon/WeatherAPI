from api.routes import weather_r
# all routes need to be included here to be created in the API
from api.app import get_app


if __name__ == "__main__":
    app = get_app()
    app.run(debug=True)  # debug only in test enviroment!
