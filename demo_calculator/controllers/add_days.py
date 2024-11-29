from flask import request, jsonify

from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.timestamp_number_request import TimestampNumberRequest
from demo_calculator.dto.datetime_response import DatetimeResponse


class AddDays(BackgroundResource):
    def post(self):
        requestData: TimestampNumberRequest = TimestampNumberRequest.parse_obj(request.json)

        service = self.Container.Calculator

        result = service.add_days(requestData.timestamp, requestData.days)

        response = DatetimeResponse(result)

        return jsonify(response)

