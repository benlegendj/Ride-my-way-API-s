'''import dependancies'''
from flask_api import FlaskAPI
app = FlaskAPI(__name__)
'''import routes'''
from ride_my_way.api.rides_views import rides
'''registering the routes to blueprints'''

app.register_blueprint(rides)
