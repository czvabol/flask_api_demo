from datetime import timedelta

class TimedeltaResponse():
    delta: timedelta
    explanation: str

    def __init__(self, delta: timedelta, explanation: str):
        self.delta = delta
        self.explanation = explanation

    def to_dict(self):
        return {
            'delta': self.delta,
            'explanation': self.explanation
        }
