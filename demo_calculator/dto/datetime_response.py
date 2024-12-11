from datetime import datetime

class DatetimeResponse:
    timestamp: datetime
    explanation: str

    def __init__(self, datetime: datetime, explanation:str):
        self.timestamp = datetime
        self.explanation = explanation
        

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'explanation': self.explanation
        }