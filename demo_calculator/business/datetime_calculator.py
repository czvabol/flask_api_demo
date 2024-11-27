from demo_calculator.abstract.abstract_datetime_calculator import AbstractDatetimeCalculator
from datetime import timedelta

class DatetimeCalculator(AbstractDatetimeCalculator):

    def time_difference(self, start, end):
        """Calculate the difference between two times
        
        Args:
            start (datetime): The start time
            end (datetime): The end time
        
        Returns:
            timedelta: The difference between the two times
        """
        return end - start

    def add_days(self, date, days):
        """Add days to a date
        
        Args:
            date (datetime): The date
            days (int): The number of days to add
        
        Returns:
            datetime: The new date
        """
        return date + timedelta(days=days)