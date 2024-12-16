from pydantic import BaseModel
from flask_restful_swagger_2 import Schema

class TwoNumbersRequest(BaseModel):
    a: float
    b: float