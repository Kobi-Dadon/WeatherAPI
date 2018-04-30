from api.app import get_app

app = get_app()

# declare namespaces here for API routings
ns_weather = app.api.namespace('weather', description='handle weather requests')
