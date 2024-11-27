from pydantic import BaseModel, validator

class PositiveNumberRequest(BaseModel):
    number: float

    @validator('number')
    def number_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('number must be positive')