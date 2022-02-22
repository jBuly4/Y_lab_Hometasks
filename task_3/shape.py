from abc import ABC, abstractmethod

class Shape:

    title = "Template shapes"

    def __init__(self, side_size: int):
        """Initialize sizes of figure."""
        self.side_size = side_size

    @staticmethod
    @abstractmethod
    def get_title():
        pass

    @classmethod
    @abstractmethod
    def get_info(cls):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


