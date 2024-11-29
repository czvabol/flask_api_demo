from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.abstract.abstract_calculator import AbstractCalculator
from demo_calculator.dto.number_reponse import NumberResponse
from flask import request, jsonify

from demo_calculator.dto.two_numbers_request import TwoNumbersRequest

class Addition(BackgroundResource):
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator

        result = service.add(requestData.a, requestData.b)

        response = NumberResponse(result)

        return jsonify(response)