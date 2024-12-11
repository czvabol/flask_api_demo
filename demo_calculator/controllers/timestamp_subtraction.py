from flask import request, jsonify

from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.two_timestamp_request import TwoTimestampRequest
from demo_calculator.dto.timedelta_response import TimedeltaResponse

class TimestampSubtraction(BackgroundResource):
    def post(self):
        requestData: TwoTimestampRequest = TwoTimestampRequest.parse_obj(request.json)

        service = self.Container.DatetimeCalculator

        result = service.time_difference(requestData.timestamp1, requestData.timestamp2)
        explanation = f' Difference between {requestData.timestamp1} and {requestData.timestamp2} is {result}'

        response = TimedeltaResponse(result, explanation).to_dict()

        return jsonify(response)
