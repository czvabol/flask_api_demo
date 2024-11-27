from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class AbstractDatetimeCalculator(ABC):
    @abstractmethod
    def time_difference(self, start:datetime, end: datetime) -> timedelta:
        """Calculate the difference between two times
        
        Args:
            start (datetime): The start time
            end (datetime): The end time
        
        Returns:
            timedelta: The difference between the two times
        """
        
    @abstractmethod
    def add_days(self, date: datetime, days: int) -> datetime:
        """Add days to a date
        
        Args:
            date (datetime): The date
            days (int): The number of days to add
        
        Returns:
            datetime: The new date
        """