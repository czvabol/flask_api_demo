from demo_calculator.abstract.abstract_calculator import AbstractCalculator


class Calculator(AbstractCalculator):

    def add(self, a: float, b: float) -> float:
        """Add two numbers

        Args:
            a (float): The first number
            b (float): The second number

        Returns:
            float: The sum of the two numbers
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers

        Args:
            a (float): The first number
            b (float): The second number

        Returns:
            float: The difference of the two numbers
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers

        Args:
            a (float): The first number
            b (float): The second number

        Returns:
            float: The product of the two numbers
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers

        Args:
            a (float): The first number
            b (float): The second number

        Returns:
            float: The quotient of the two numbers
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Raise a number to a power

        Args:
            a (float): The base number
            b (float): The exponent

        Returns:
            float: The result of raising the base to the exponent
        """
        return a ** b

    def sqrt(self, a: float) -> float:
        """Calculate the square root of a number

        Args:
            a (float): The number to take the square root of

        Returns:
            float: The square root of the number
        """
        return a ** 0.5