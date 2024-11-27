from pydantic import BaseModel, validator
from datetime import datetime

class TimestampNumberRequest(BaseModel):
    timestamp: datetime
    number: int

    @validator('timestamp')
    def validate_timestamp(cls, value):
        if value < datetime.now():
            raise ValueError('timestamp must be in the future')
        return value

    @validator('number')
    def validate_number(cls, value):
        if value < 0:
            raise ValueError('number must be positive')
        return value