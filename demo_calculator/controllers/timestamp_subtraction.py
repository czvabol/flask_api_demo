from flask import request, jsonify
from flasgger import swag_from

from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.two_timestamp_request import TwoTimestampRequest
from demo_calculator.dto.timedelta_response import TimedeltaResponse

class TimestampSubtraction(BackgroundResource):
    @swag_from({
        'tags': ['Timestamp Subtraction'],
        'description': 'Subtract two timestamps',
        'parameters': [
            {
                'name': 'body',
                'description': 'Two timestamps',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'timestamp1': {'type': 'string', 'description': 'First timestamp'},
                        'timestamp2': {'type': 'string', 'description': 'Second timestamp'}
                    },
                    'required': ['timestamp1', 'timestamp2']
                }
            }
        ],
        'responses': {
            '200': {
                'description': 'Result of subtraction',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'result': {'type': 'string', 'description': 'Result of subtraction'},
                        'explanation': {'type': 'string', 'description': 'Explanation of the result'}
                    }
                }
            }
        }
    })
    def post(self):
        requestData: TwoTimestampRequest = TwoTimestampRequest.parse_obj(request.json)

        service = self.Container.DatetimeCalculator

        result = service.time_difference(requestData.timestamp1, requestData.timestamp2)
        explanation = f' Difference between {requestData.timestamp1} and {requestData.timestamp2} is {result}'

        response = TimedeltaResponse(result, explanation).to_dict()

        return jsonify(response)
