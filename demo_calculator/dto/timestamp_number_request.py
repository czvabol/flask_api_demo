from pydantic import BaseModel, validator
from datetime import datetime
from pydantic import Field

class TimestampNumberRequest(BaseModel):
    stamp: datetime
    days: int

    @validator('stamp')
    def validate_timestamp(cls, value):
        if value < datetime.now():
            raise ValueError('timestamp must be in the future')
        return value

    @validator('days')
    def validate_number(cls, value):
        if value < 0:
            raise ValueError('number must be positive')
        return value