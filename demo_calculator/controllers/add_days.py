from flask import request, jsonify

from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.timestamp_number_request import TimestampNumberRequest
from demo_calculator.dto.datetime_response import DatetimeResponse


class AddDays(BackgroundResource):
    def post(self):
        requestData: TimestampNumberRequest = TimestampNumberRequest.parse_obj(request.json)

        service = self.Container.DatetimeCalculator
        logger = self.Container.Logger

        result = service.add_days(requestData.stamp, requestData.days)
        explanation = f'{requestData.stamp} + {requestData.days} days = {result}'
        logger.debug(explanation)

        response = DatetimeResponse(result, explanation).to_dict()

        return jsonify(response)

