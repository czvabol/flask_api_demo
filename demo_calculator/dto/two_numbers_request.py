from pydantic import BaseModel

class TwoNumbersRequest(BaseModel):
    a: float
    b: float