'''import dependancies'''
import datetime
from flask import jsonify, Blueprint, request, make_response, session
from ride_my_way import app
from ride_my_way.api.models import RideMyWay


rides = Blueprint('rides', __name__)
ride_my_way = RideMyWay()





@app.route('/api/v1/rides', methods=['POST'])
def add_ride():
    '''Function to add a ride'''
    sent_data = request.get_json(force=True)
    data = {
        'ride_id': len(ride_my_way.rides_list) + 1,
        'starting_point': sent_data.get('starting_point'),
        'destination': sent_data.get('destination'),
        'date': sent_data.get('date'),
        'time': sent_data.get('time')

    }
    if ride_my_way.add_ride_validation(data):
        ride_my_way.create_rides(data)
        response = jsonify({
            'ride_id': data['ride_id'],
            'starting_point': data['starting_point'],
            'destination': data['destination'],
            'date': data['date'],
            'time': data['time'],
            'available': True
        })
        response.status_code = 201
        return response
    else:
        return jsonify({"message": "Please enter correct ride details"})


