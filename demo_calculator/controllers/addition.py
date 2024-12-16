from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.abstract.abstract_calculator import AbstractCalculator
from demo_calculator.dto.number_reponse import NumberResponse
from flask import request, jsonify
from flasgger import swag_from

from demo_calculator.dto.two_numbers_request import TwoNumbersRequest

class Addition(BackgroundResource):
    @swag_from({
        'tags': ['Addition'],
        'description': 'Add two numbers',
        'parameters': [
            {
                'name': 'body',
                'description': 'Two numbers',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'a': {'type': 'number', 'description': 'First number'},
                        'b': {'type': 'number', 'description': 'Second number'}
                    },
                    'required': ['a', 'b']
                }            }
        ],
        'responses': {
            '200': {
                'description': 'Result of addition',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'result': {'type': 'number', 'description': 'Result of addition'},
                        'explanation': {'type': 'string', 'description': 'Explanation of the result'}
                    }
                }
            }
        }
    })
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator
        logger = self.Container.Logger

        result = service.add(requestData.a, requestData.b)
        explanation = f'{requestData.a} + {requestData.b} = {result}'
        logger.debug(explanation)

        response = NumberResponse(result, explanation=explanation).to_dict()

        return jsonify(response)