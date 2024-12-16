from demo_calculator.abstract.abstract_draw_service import AbstractDrawService
import random


class DrawService(AbstractDrawService):
    def draw_winner(self, members: list) -> str:
        random.shuffle(members)
        return members[0]