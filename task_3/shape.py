class Shape:

    title = "Template shapes"

    def __init__(self, side_size: int):
        """Initialize sizes of figure."""
        self.side_size = side_size

    @staticmethod
    def get_title():
        pass

    @classmethod
    def get_info(cls):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


