from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    @abstractmethod
    def add(self, a: float, b:float) -> float:
        """add two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """

    @abstractmethod
    def subtract(self, a:float, b: float) -> float:
        """subtract two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """

    @abstractmethod
    def multiply(self, a:float, b:float) -> float:
        """multiply two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """ 

    @abstractmethod
    def divide(self, a:float, b:float) -> float:
        """divide two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """

    @abstractmethod
    def power(self, a:float, b:float) -> float:
        """power of two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """

    @abstractmethod
    def sqrt(self, a:float) -> float:
        """square root of a number

        Args:
            a (float): _description_
        """