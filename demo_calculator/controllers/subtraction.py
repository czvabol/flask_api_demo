from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.two_numbers_request import TwoNumbersRequest
from demo_calculator.dto.number_reponse import NumberResponse
from demo_calculator.abstract.abstract_calculator import AbstractCalculator

from flask import request, jsonify

class Subtraction(BackgroundResource):
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator

        result = service.subtract(requestData.a, requestData.b)
        explanation = f'{requestData.a} - {requestData.b} = {result}'

        response = NumberResponse(result, explanation).to_dict()

        return jsonify(response)