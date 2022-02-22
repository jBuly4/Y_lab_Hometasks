import tkinter as tk
from typing import Type

from shape import Shape


class My_3D_Renderer:
    """Render window for different figures"""

    def __init__(self, text: str, figure: Type[Shape]):
        self.text = text
        self.figure = figure
        self.sizes = None # ??
        self.create_window()

    @staticmethod
    def get_lst_methods(class_name: Type[Shape]) -> list:
        """Returns list of method for a Class."""
        return [method for method in dir(class_name) if not method.startswith('__')]

    @staticmethod
    def get_sizes():
        return self.sizes

    def create_window(self):
        win = tk.Toplevel()  # should be self inside parentheses?
        win.title(f"{self.text} calculations")
        win.geometry("600x600")

        frame_1 = tk.Frame(win)
        frame_1.pack()

        label = tk.Label(frame_1, text="List of options:", font=15, width=12)
        label.pack(side="left")

        lb = tk.Listbox(frame_1)
        lb.pack(side="left", pady=5, padx=1)

        frame_2 = tk.Frame(win)
        frame_2.pack()

        btn = tk.Button(frame_2, text="Go!")
        btn.pack(side="right")

        btn.bind("<Button-1>", lambda event: self.calculate_n_draw(event, self.sizes, self.text, win))  # calculate
        # and draw
        if self.text == "Sphere":
            Fill_window_sphere.fill(frame_2, self.sizes, self.get_lst_methods(self))
        elif self.text == "Cube":
            Fill_window_cube.fill(frame_2, self.sizes, self.get_lst_methods(self))
        elif self.text == "Parallelepiped":
            Fill_window_parallelepiped.fill(frame_2, self.sizes, self.get_lst_methods(self))
        elif self.text == "Pyramid":
            Fill_window_pyramid.fill(frame_2, self.sizes, self.get_lst_methods(self))
        elif self.text == "Cylinder":
            Fill_window_Cylinder.fill(frame_2, self.sizes, self.get_lst_methods(self))
        elif self.text == "Cone":
            Fill_window_Cone.fill(frame_2, self.sizes, self.get_lst_methods(self))


class Fill_window_sphere:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert radius of Sphere ", width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)


class Fill_window_cube:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes: tk.Entry, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert radius of Cube ", width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)


class Fill_window_parallelepiped:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes: tk.Entry, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert side 1\n and side 2\nand side 3 of Parallelepiped\n with space ",
                               width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)


class Fill_window_pyramid:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes: tk.Entry, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert base sides a, b\n and height c of Pyramid\n with space ",
                               width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)


class Fill_window_Cylinder:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes: tk.Entry, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert radius a\n and height b of Cylinder\n with space ",
                               width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)


class Fill_window_Cone:
    @classmethod
    def fill(cls, frame: tk.Frame, lb: tk.Listbox, sizes: tk.Entry, method_lst: list):
        indx = 0
        for method in method_lst:
            lb.insert(indx, method)
            indx += 1

        label_sizes = tk.Label(frame, text=f"Insert radius a\n and height b of Cone\n with space ",
                               width=19)
        label_sizes.pack(side="left", pady=5, padx=5)
        sizes = tk.Entry(frame, width=21)
        sizes.pack(fill="x", side="left", pady=5, padx=5)