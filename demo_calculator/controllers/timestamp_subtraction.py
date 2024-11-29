from flask import request, jsonify

from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.two_timestamp_request import TwoTimestampRequest
from demo_calculator.dto.timedelta_response import TimedeltaResponse

class TimestampSubtraction(BackgroundResource):
    def post(self):
        requestData: TwoTimestampRequest = TwoTimestampRequest.parse_obj(request.json)

        service = self.Container.Calculator

        result = service.subtract(requestData.a, requestData.b)

        response = TimedeltaResponse(result)

        return jsonify(response)
