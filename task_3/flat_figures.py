from math import radians, sin, cos
from shape import Shape


class Circle(Shape):
    title = "Circle"

    def __init__(self, radius: int, pi=3.14):
        super().__init__(radius)
        self.pi = pi

    @staticmethod
    def get_title() -> str:
        return Circle.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Circle.get_title()}. To initialize please insert radius and value of pi.\"" \
               f"\nMethods:\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Diameter;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> float:
        return self.pi * self.side_size ** 2

    def get_perimeter(self) -> float:
        return 2 * self.pi * self.side_size

    def get_diameter(self) -> int:
        return 2 * self.side_size


class Square(Shape):
    title = "Square"

    def __init__(self, side_size: int):
        super().__init__(side_size)

    @staticmethod
    def get_title() -> str:
        return Square.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Square.get_title()}. To initialize please insert size of side.\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Diagonal;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> int:
        return self.side_size ** 2

    def get_perimeter(self) -> int:
        return 4 * self.side_size

    def get_diagonal(self) -> float:
        return self.side_size * (2 ** 0.5)


class Rectangle(Square):
    title = "Rectangle"

    def __init__(self, x: int, y: int):
        super().__init__(x)
        self.other_side_size = y

    @staticmethod
    def get_title() -> str:
        return Rectangle.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Rectangle.get_title()}. To initialize please insert size of sides.\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Diagonal;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> int:
        return self.side_size * self.other_side_size

    def get_perimeter(self) -> int:
        return 2 * self.side_size + 2 * self.other_side_size

    def get_diagonal(self) -> float:
        return (self.side_size ** 2 + self.other_side_size ** 2) ** 0.5


class Triangle(Shape):
    title = "Triangle"

    def __init__(self, a: int, b: int, c: int):
        super().__init__(a)
        self.b = b
        self.c = c
        self.half_perim = (self.side_size + self.b + self.c) * 0.5

    @staticmethod
    def get_title() -> str:
        return Triangle.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Triangle.get_title()}. To initialize please insert a, b and c.\"" \
               f"\nMethods:\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Height based on a;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> float:
        return (self.half_perim *
                (self.half_perim - self.side_size) *
                (self.half_perim - self.b) *
                (self.half_perim - self.c)) ** 0.5

    def get_perimeter(self) -> int:
        return self.side_size + self.b + self.c

    def get_height(self) -> float:
        return 2 * self.get_area() / self.side_size


class Trapezoid(Shape):
    title = "Trapezoid"

    def __init__(self, a: int, b: int, c: int, d: int):
        super().__init__(a)
        self.b = b
        self.c = c
        self.d = d
        self.h = (((self.side_size - self.b) ** 2 - self.d ** 2 + self.c ** 2) / (2 * (a - b)))

    @staticmethod
    def get_title() -> str:
        return Trapezoid.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Trapezoid.get_title()}. To initialize please insert bases a, b and side sizes c, d.\"" \
               f"\nMethods:\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Height;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> float:
        return (self.side_size + self.b) * self.get_height() * 0.5

    def get_perimeter(self) -> int:
        return self.side_size + self.b + self.c + self.d

    def get_height(self) -> float:
        return (self.c ** 2 - self.h ** 2) ** 0.5


class Rhombus(Shape):
    title = "Rhombus"

    def __init__(self, side_size: int, angle: int):
        super().__init__(side_size)
        if angle > 90:
            self.angle = radians(360 - 2 * angle)
            self.other_angle = radians(angle)
        else:
            self.angle = radians(angle)
            self.other_angle = radians(360 - 2 * angle)

    @staticmethod
    def get_title() -> str:
        return Rhombus.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Rhombus.get_title()}. To initialize please insert size of side and angle (degrees).\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Perimeter;\n\t" \
               f"[*] Diagonals;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> int:
        return self.side_size ** 2 * sin(self.angle)

    def get_perimeter(self) -> int:
        return 4 * self.side_size

    def get_diagonals(self) -> float:
        diag_1 = self.side_size * (2 + 2 * cos(self.angle)) ** 0.5
        diag_2 = self.side_size * (2 - 2 * cos(self.other_angle)) ** 0.5
        return diag_1, diag_2
