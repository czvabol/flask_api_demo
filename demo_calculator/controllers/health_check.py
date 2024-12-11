from flask_restful import Resource
from flask import jsonify


class HealthCheck(Resource):
    def post(self):
        return jsonify("OK")
