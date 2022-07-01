class Points:
    def __init__(self, object):
        """
        Initializing our object with points
        :param object: list of points
        """
        self.points = []
        if type(object) == list:
            self.add_many(object)
        elif type(object) == tuple:
            self.add_one(object)

    def add_many(self, points: list):
        """
        Add new list of points
        :param points: list of points with x and y coordinates
        """
        self.points = self.points + points

    def add_one(self, point: tuple):
        """
        Add one point
        :param point: x and y coordinates (tuple)
        """
        self.points.append(point)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item: int):
        """
        Work with class object through indexes
        :param item: index
        :return: value at index
        """
        return self.points[item]

    def __str__(self):
        """
        Print points in one line
        :return: points in string
        """
        res = ""
        for point in self.points:
            res += str(point) + " "
        return res.rstrip()


