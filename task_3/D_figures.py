from math import radians, sin, cos
from flat_figures import Circle
from shape import Shape


class Sphere(Circle):
    title = "Sphere"

    def __init__(self, radius: int, pi=3.14):
        super().__init__(radius)
        self.pi = pi

    @staticmethod
    def get_title() -> str:
        return Sphere.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Sphere.get_title()}. To initialize please insert radius and value of pi.\"" \
               f"\nMethods:\n\t[*] Area;\n\t[*] Diameter;\n\t[*] Title."

    def get_area(self) -> float:
        return 4 * self.pi * self.side_size**2

    def get_diameter(self) -> int:
        return 2 * self.side_size


class Cube(Shape):
    title = "Cube"

    def __init__(self, side_size: int):
        super().__init__(side_size)

    @staticmethod
    def get_title() -> str:
        return Cube.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Cube.get_title()}. To initialize please insert size of side.\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Perimeter;\n\t[*] Title."

    def get_area(self) -> int:
        return 6 * self.side_size**2

    def get_perimeter(self) -> int:
        return 12 * self.side_size


class Parallelepiped(Cube):
    title = "Parallelepiped"

    def __init__(self, x: int, y: int, z: int):
        super().__init__(x)
        self.y = y
        self.z = z

    @staticmethod
    def get_title() -> str:
        return Parallelepiped.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Parallelepiped.get_title()}. To initialize please insert size of sides.\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Perimeter;\n\t[*] Info;\n\t[*] Title."

    def get_area(self) -> int:
        return (self.side_size * self.y) * 2 + (self.side_size * self.z) * 2 + (self.y * self.z) * 2

    def get_perimeter(self) -> int:
        return 4 * self.side_size + 4 * self.y + 4 * self.z

    def get_diagonal(self) -> float:
        return (self.side_size**2 + self.y**2 + self.z**2)**0.5


class Pyramid(Shape):
    title = "Pyramid"

    def __init__(self, a: int, b: int, height: int):
        """
        :param a: side of pyramid base
        :param b: side of pyramid base
        :param height: height
        """
        super().__init__(a)
        self.b = b
        self.height = height

    @staticmethod
    def get_title() -> str:
        return Pyramid.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Pyramid.get_title()}. To initialize please insert base sides a, b and height c.\"" \
               f"\nMethods:\n\t[*] Area of base;\n\t[*] Height;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> float:
        return self.side_size * self.b

    def get_height(self) -> int:
        return self.height

    def get_base(self):
        return self.side_size, self.b


class Cylinder(Circle):
    title = "Cylinder"

    def __init__(self, radius: int, height: int, pi=3.14):
        """
        :param radius: radius of base
        :param height: height
        """
        super().__init__(radius)
        self.height = height
        self.pi = pi

    @staticmethod
    def get_title() -> str:
        return Cylinder.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Cylinder.get_title()}. To initialize please insert radius a and height b and pi" \
               f" [optional]\nMethods:\n\t[*] Area;\n\t[*] Height;\n\t[*] Volume;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> float:
        return (2 * self.pi * self.side_size**2) + 2 * self.pi * self.side_size * self.height

    def get_height(self) -> float:
        return self.height

    def get_volume(self) -> float:
        return self.pi * self.side_size**2 * self.height


class Cone(Shape):
    title = "Cone"

    def __init__(self, radius: int, height: int):
        super().__init__(radius)
        self.height = height
        self.pi = 3.14

    @staticmethod
    def get_title() -> str:
        return Cone.title

    @classmethod
    def get_info(cls) -> str:
        return f"Figure {Cone.get_title()}. To initialize please insert radius and height.\nMethods:" \
               f"\n\t[*] Area;\n\t[*] Volume;\n\t[*] Info; \n\t[*] Title."

    def get_area(self) -> int:
        return self.pi * self.side_size * (self.side_size**2 + self.height**2)**0.5

    def get_volume(self) -> int:
        return  self.get_area() * self.height / 3

    def get_radius(self):
        return self.side_size

    def get_height(self):
        return self.height
