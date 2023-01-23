from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.foods import Food

jpFood_api = Blueprint('jpFood_api', __name__,
                   url_prefix='/api/jpFood')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(jpFood_api)

class jpFoodAPI:        
    class _Get(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            foodName = body.get('Food')
            if foodName is None:
                return {'message': f'Food is missing, please select a food.'}, 210
            # validate uid
            
            ''' Additional garbage error checking '''
            # set password if provided
            foodPortions = body.get('Food')
            if foodPortions is None:
                return {'message': f'Portions are missing, please input portions.'}, 210
            # convert to date type
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            foods = foods.get('Food')
            # success returns json of user

    class _Read(Resource):
        def get(self):
            foods = Food.query.all()    # read/extract all users from database
            json_ready = [food.read() for food in foods]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Get, '/get')
    api.add_resource(_Read, '/')