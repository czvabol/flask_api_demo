from flask import request, jsonify
from flasgger import swag_from
from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.timestamp_number_request import TimestampNumberRequest
from demo_calculator.dto.datetime_response import DatetimeResponse


class AddDays(BackgroundResource):
    @swag_from({
        'description': 'Add days to a timestamp',
        'tags': ['Add days'],
        'parameters': [
            {
                'name': 'body',
                'description': 'Timestamp and number of days',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'stamp': {'type': 'string', 'description': 'Timestamp'},
                        'days': {'type': 'number', 'description': 'Number of days to add'}
                    },
                    'required': ['stamp', 'days']
                }
            }
        ],
        'responses': {
            '200': {
                'description': 'Result of addition',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'result': {'type': 'string', 'description': 'Result of addition'},
                        'explanation': {'type': 'string', 'description': 'Explanation of the result'}
                    }
                }
            }
        }   
    })
    def post(self):
        requestData: TimestampNumberRequest = TimestampNumberRequest.parse_obj(request.json)

        service = self.Container.DatetimeCalculator
        logger = self.Container.Logger

        result = service.add_days(requestData.stamp, requestData.days)
        explanation = f'{requestData.stamp} + {requestData.days} days = {result}'
        logger.debug(explanation)

        response = DatetimeResponse(result, explanation).to_dict()

        return jsonify(response)

