from flask_restful import Resource
from flask import jsonify
from flasgger import swag_from


class HealthCheck(Resource):
    @swag_from({
        'tags': ['Health Check'],
        'description': 'Health check',
        'parameters': [],
        
        'responses': {
            200: {
                'description': 'Health check',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'string',
                            'example': 'OK'
                        }
                    }
                }
            }
        }
    })
    def post(self):
        return jsonify("OK")
