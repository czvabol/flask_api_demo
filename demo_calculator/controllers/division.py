from flask import request, jsonify
from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.dto.two_numbers_request import TwoNumbersRequest
from demo_calculator.dto.number_reponse import NumberResponse
from demo_calculator.abstract.abstract_calculator import AbstractCalculator

class Division(BackgroundResource):
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator
        logger = self.Container.Logger

        result = service.divide(requestData.a, requestData.b)
        explanation = f'{requestData.a} / {requestData.b} = {result}'
        logger.debug(explanation)

        response = NumberResponse(result, explanation).to_dict()

        return jsonify(response)