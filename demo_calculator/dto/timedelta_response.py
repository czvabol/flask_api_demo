from datetime import timedelta

class TimedeltaResponse():
    delta: str
    explanation: str

    def __init__(self, delta: timedelta, explanation: str):
        self.delta = str(delta)
        self.explanation = explanation

    def to_dict(self):
        return {
            'delta': self.delta,
            'explanation': self.explanation
        }
