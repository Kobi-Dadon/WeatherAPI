from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.api = Api(app, title='Simple Weather API')


def get_app():
    global app
    return app
