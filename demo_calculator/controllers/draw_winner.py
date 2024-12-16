from flask import request, jsonify
from flasgger import swag_from
from demo_calculator.dto.members import Members

from demo_calculator.controllers.background_resource import BackgroundResource

class WinnerDraw(BackgroundResource):
    def post(self):
        
        members_request: Members = Members.parse_obj(request.json)
        service = self.Container.DrawService

        winner = service.draw_winner(members_request.members)
        return jsonify({'winner': winner})