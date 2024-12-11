from demo_calculator.controllers.background_resource import BackgroundResource
from demo_calculator.abstract.abstract_calculator import AbstractCalculator
from demo_calculator.dto.number_reponse import NumberResponse
from flask import request, jsonify

from demo_calculator.dto.two_numbers_request import TwoNumbersRequest

class Addition(BackgroundResource):
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator
        logger = self.Container.Logger

        result = service.add(requestData.a, requestData.b)
        explanation = f'{requestData.a} + {requestData.b} = {result}'
        logger.debug(explanation)

        response = NumberResponse(result, explanation=explanation).to_dict()

        return jsonify(response)