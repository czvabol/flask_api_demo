from demo_calculator.abstract.abstract_calculator import AbstractCalculator
from demo_calculator.abstract.abstract_datetime_calculator import AbstractDatetimeCalculator
from demo_calculator.abstract.abstract_draw_service import AbstractDrawService
import logging

class ServiceContainer:
    Calculator: AbstractCalculator
    DatetimeCalculator: AbstractDatetimeCalculator
    DrawService: AbstractDrawService
    Logger: logging.Logger