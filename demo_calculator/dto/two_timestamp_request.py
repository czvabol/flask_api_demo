from pydantic import BaseModel, validator
from datetime import datetime

class TwoTimestampRequest(BaseModel):
    timestamp1: datetime
    timestamp2: datetime

    def to_dict(self):
        return {
            'timestamp1': self.timestamp1,
            'timestamp2': self.timestamp2
        }

    @validator('timestamp2')
    def validate_timestamps(cls, values):
        timestamp1, timestamp2 = values.get('timestamp1'), values.get('timestamp2')
        if timestamp1 > timestamp2:
            raise ValueError('timestamp1 must be before timestamp2')
        return values

    def __str__(self):
        return f'TwoTimestampRequest({self.timestamp1}, {self.timestamp2})'

    def __repr__(self):
        return self.__str__()