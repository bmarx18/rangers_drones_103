from flask import Blueprint, request, jsonify
from drone_inventory.helpers import token_required
from drone_inventory.models import db, Drone, drone_schema, drones_schema


api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_data):
    return { 'some': 'value' }

@api.route('/drones', methods = ['POST'])
@token_required
def create_drone(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    camera_quality = request.json['camera_quality']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_production = request.json['cost_of_production']
    series = request.json['series']
    user_token = current_user_token.token

    print(f'User Token: {current_user_token.token}')

    drone = Drone(name, description, price, camera_quality, flight_time, max_speed, dimensions, weight, cost_of_production, series, user_token=user_token)

    db.session.add(drone)
    db.session.commit()

    response = drone_schema.dump(drone)

    return jsonify(response)

@api.route('/drones', methods = ['GET'])
@token_required
def get_drones(current_user_token):
    owner = current_user_token.token
    drones = Drone.query.filter_by(user_token = owner).all()
    response = drone_schema.dump(drones)
    return jsonify(response)


@api.route('/drones/<id>', methods = ["GET"])
@token_required
def get_drone(current_user_token, id):
    owner = current_user_token
    if owner == current_user_token.token:
        drone = Drone.query.get(id)
        response = drone_schema.dump(drone)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401
