from flask import Flask
from flask_restful import Resource, Api
# from flask_restful_swagger_2 import swagger, Api
import logging
from logging.handlers import RotatingFileHandler
import json

from demo_calculator.business.calculator import Calculator
from demo_calculator.business.datetime_calculator import DatetimeCalculator
from demo_calculator.models.service_container import ServiceContainer
from demo_calculator.business.draw_service import DrawService

from demo_calculator.controllers.addition import Addition
from demo_calculator.controllers.subtraction import Subtraction
from demo_calculator.controllers.multiplication import Multiplication
from demo_calculator.controllers.division import Division
from demo_calculator.controllers.add_days import AddDays
from demo_calculator.controllers.timestamp_subtraction import TimestampSubtraction
from demo_calculator.controllers.health_check import HealthCheck
from demo_calculator.controllers.draw_winner import WinnerDraw

from flasgger import Swagger

def getLoggingLevel(config:dict)->int:
    level = logging.WARNING
    try:
        levelString = config['Application']['loggingLevel']
        level = logging.getLevelName(levelString)
        if level is not  int:
            level = logging.WARNING
    except Exception:
        level = logging.WARNING

    return level


app = Flask(__name__)

with open('config.json', 'rt') as f:
    config = json.loads(f.read())

logging.basicConfig(
        handlers=[RotatingFileHandler('test.log', maxBytes=1e8, backupCount=10)],
        level=getLoggingLevel(config),
        format="[%(asctime)s] %(levelname)s [%(processName)s %(threadName)s] [%(name)s.%(funcName)s:%(lineno)d]  %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S'
    )

logger = logging.getLogger('demo_calulator')

# start services
calculator = Calculator()
datetime_calculator = DatetimeCalculator()
draw_service = DrawService()

#create container
container = ServiceContainer()
container.Calculator = calculator
container.DatetimeCalculator = datetime_calculator
container.DrawService = draw_service
container.Logger = logger

#create endpoints
# api = Api(app, api_version='0.1', api_spec_url='/api/swagger')
api = Api(app)
swagger = Swagger(app, config={
    'headers': [],
    'specs':[
        {
            'endpoint': 'apispec_1',
            'route': '/apispec_1.json',
            'rule_filter': lambda rule: True,
            'model_filter': lambda tag: True
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/swagger/'
})

api_args = {'Container': container}

api.add_resource(Addition, '/add', resource_class_kwargs=api_args)
api.add_resource(Subtraction, '/subtract', resource_class_kwargs=api_args)
api.add_resource(Multiplication, '/multiply', resource_class_kwargs=api_args)
api.add_resource(Division, '/divide', resource_class_kwargs=api_args)
api.add_resource(AddDays, '/add_days', resource_class_kwargs=api_args)
api.add_resource(TimestampSubtraction, '/subtract_timestamp', resource_class_kwargs=api_args)
api.add_resource(HealthCheck, '/health')
api.add_resource(WinnerDraw, '/draw_winner', resource_class_kwargs=api_args)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)