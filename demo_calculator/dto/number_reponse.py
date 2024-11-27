class NumberResponse():
    result: float
    explanation: str

    def __init__(self, result: float, explanation: str):
        self.result = result
        self.explanation = explanation
        
    def to_dict(self):
        return {
            'result': self.result,
            'explanation': self.explanation
        }
