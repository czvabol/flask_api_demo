from demo_calculator.abstract.abstract_calculator import AbstractCalculator
from demo_calculator.abstract.abstract_datetime_calculator import AbstractDatetimeCalculator
import logging

class ServiceContainer:
    Calculator: AbstractCalculator
    DatetimeCalculator: AbstractDatetimeCalculator
    Logger: logging.Logger