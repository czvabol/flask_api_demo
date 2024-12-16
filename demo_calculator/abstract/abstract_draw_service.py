from abc import ABC, abstractmethod

class AbstractDrawService(ABC):
    @abstractmethod
    def draw_winner(self, members: list) -> str:
        """Draw a winner from a list of members

        Args:
            members (list): List of members

        Returns:
            str: Winner
        """