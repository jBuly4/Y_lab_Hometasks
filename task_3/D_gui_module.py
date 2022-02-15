import tkinter as tk

from D_figures import Sphere, Cube, Parallelepiped, Pyramid, Cylinder, Cone

btn_names_main = [class_name.get_title() for class_name in [Sphere, Cube, Parallelepiped, Pyramid, Cylinder, Cone]]


class My_3D_GUI(tk.Tk):
    """Class for processing 3D figures"""
    def __init__(self):
        super().__init__()
        self.btns = [self.create_btn(text) for text in btn_names_main]

        for btn in self.btns:
            btn.pack()

    def create_btn(self, text):
        return tk.Button(self, text=text, width=30, height=5, command=lambda t=text: self.render_results(text))

    def render_results(self, text: str):
        """Process events and calculations for different figures"""
        indx = 0
        win = tk.Toplevel(self)
        win.title(f"{text} calculations")
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

        btn.bind("<Button-1>", lambda event: self.calculate_n_draw(event, sizes, text, win))

        if text == Sphere.get_title():
            method_lst = self.get_lst_methods(Sphere)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert radius of {text} ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Cube.get_title():
            method_lst = self.get_lst_methods(Cube)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side of {text} ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Parallelepiped.get_title():
            method_lst = self.get_lst_methods(Parallelepiped)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side 1\n and side 2\nand side 3 of {text}\n with space ",
                                   width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Pyramid.get_title():
            method_lst = self.get_lst_methods(Pyramid)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert base sides a, b\n and height c of {text}\n with space ",
                                   width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Cylinder.get_title():
            method_lst = self.get_lst_methods(Cylinder)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert radius a\n and height b of {text}\n with space ",
                                   width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Cone.get_title():
            method_lst = self.get_lst_methods(Cone)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert radius a\n and height b of {text}\n with space ",
                                   width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

    def calculate_n_draw(self, event, sizes, text, win):
        """Make calculations and draw figures."""
        canvas_frame = tk.Frame(win)
        canvas_frame.pack()
        canvas = tk.Canvas(canvas_frame)
        canvas.pack(fill="x")

        if text == Sphere.get_title():
            try:
                sphere = Sphere(int(sizes.get()))
                lb_res = tk.Label(win, text=f"Area {sphere.get_area()}\nDiameter {sphere.get_diameter()}", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, sphere)

            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Cube.get_title():
            try:
                cube = Cube(int(sizes.get()))
                lb_res = tk.Label(win, text=f"Area {cube.get_area()}\nPerimeter {cube.get_perimeter()}\n", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, cube)
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Parallelepiped.get_title():
            try:
                x, y, z = map(int, sizes.get().split())
                parallelepiped = Parallelepiped(x, y, z)
                lb_res = tk.Label(win, text=f"Area {parallelepiped.get_area()}\nPerimeter {parallelepiped.get_perimeter()}\n"
                                            f"Diagonal {parallelepiped.get_diagonal()}", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, parallelepiped)
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Pyramid.get_title():
            try:
                a, b, c = map(int, sizes.get().split())
                pyramid = Pyramid(a, b, c)
                lb_res = tk.Label(win, text=f"Area {pyramid.get_area()}\n" \
                                            f"Heigt {pyramid.get_height()}", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, pyramid)
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error or Wrong sides!")
                lb_err.pack()

        elif text == Cylinder.get_title():
            try:
                a, b = map(int, sizes.get().split())
                cylinder = Cylinder(a, b)
                lb_res = tk.Label(win, text=f"Area {cylinder.get_area()}\nVolume {cylinder.get_volume()}" \
                                            f"Height {cylinder.get_height()}", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, cylinder)
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Cone.get_title():
            try:
                a, height = map(int, sizes.get().split())
                cone = Cone(a, height)
                lb_res = tk.Label(win, text=f"Area {cone.get_area()}\nVolume {cone.get_volume()}\n", bg="white")
                lb_res.pack(side="bottom")
                self.draw_figure(canvas, cone)
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

    @staticmethod
    def get_lst_methods(class_name) -> list:
        """Returns list of method for a Class."""
        return [method for method in dir(class_name) if not method.startswith('__')]

    def draw_figure(self, canvas, instance):
        """Draw all figures depending on instance."""
        x_centre = y_centre = 300 / 2
        if instance.get_title() == Cube.get_title():
            canvas.create_rectangle(0.9 * (x_centre - instance.get_perimeter() / 12),
                                    0.9 * (y_centre - instance.get_perimeter() / 12),
                                    0.9 * (x_centre + instance.get_perimeter() / 12),
                                    0.9 * (y_centre + instance.get_perimeter() / 12),
                                    outline="black")
            canvas.create_line(0.9 * (x_centre - instance.get_perimeter() / 12),
                               0.9 * (y_centre - instance.get_perimeter() / 12),
                               x_centre - instance.get_perimeter() / 12 + 20,
                               y_centre - instance.get_perimeter() / 12 + 20)
            canvas.create_line(0.9 * (x_centre - instance.get_perimeter() / 12),
                               0.9 * (y_centre + instance.get_perimeter() / 12),
                               x_centre - instance.get_perimeter() / 12 + 20,
                               y_centre + instance.get_perimeter() / 12 + 20)
            canvas.create_line(0.9 * (x_centre + instance.get_perimeter() / 12),
                               0.9 * (y_centre - instance.get_perimeter() / 12),
                               x_centre + instance.get_perimeter() / 12 + 20,
                               y_centre - instance.get_perimeter() / 12 + 20)
            canvas.create_line(0.9 * (x_centre + instance.get_perimeter() / 12),
                               0.9 * (y_centre + instance.get_perimeter() / 12),
                               x_centre + instance.get_perimeter() / 12 + 20,
                               y_centre + instance.get_perimeter() / 12 + 20,
                               dash=(10, 10))
            canvas.create_rectangle(x_centre - instance.get_perimeter() / 12 + 20,
                                    y_centre - instance.get_perimeter() / 12 + 20,
                                    x_centre + instance.get_perimeter() / 12 + 20,
                                    y_centre + instance.get_perimeter() / 12 + 20,
                                    outline="black")

        elif instance.get_title() == Parallelepiped.get_title():
            canvas.create_rectangle(0.9 * (x_centre - instance.get_perimeter() / 12),
                                    0.9 * (y_centre - instance.get_perimeter() / 12),
                                    0.9 * (x_centre + instance.get_perimeter() / 12),
                                    0.9 * (y_centre + instance.get_perimeter() / 12),
                                    outline="black")
            canvas.create_line(0.9 * (x_centre - instance.get_perimeter() / 12),
                               0.9 * (y_centre - instance.get_perimeter() / 12),
                               x_centre - instance.get_perimeter() / 12 + instance.z,
                               y_centre - instance.get_perimeter() / 12 + instance.z)
            canvas.create_line(0.9 * (x_centre - instance.get_perimeter() / 12),
                               0.9 * (y_centre + instance.get_perimeter() / 12),
                               x_centre - instance.get_perimeter() / 12 + instance.z,
                               y_centre + instance.get_perimeter() / 12 + instance.z)
            canvas.create_line(0.9 * (x_centre + instance.get_perimeter() / 12),
                               0.9 * (y_centre - instance.get_perimeter() / 12),
                               x_centre + instance.get_perimeter() / 12 + instance.z,
                               y_centre - instance.get_perimeter() / 12 + instance.z)
            canvas.create_line(0.9 * (x_centre + instance.get_perimeter() / 12),
                               0.9 * (y_centre + instance.get_perimeter() / 12),
                               x_centre + instance.get_perimeter() / 12 + instance.z,
                               y_centre + instance.get_perimeter() / 12 + instance.z,
                               dash=(10, 10))
            canvas.create_rectangle(x_centre - instance.get_perimeter() / 12 + instance.z,
                                    y_centre - instance.get_perimeter() / 12 + instance.z,
                                    x_centre + instance.get_perimeter() / 12 + instance.z,
                                    y_centre + instance.get_perimeter() / 12 + instance.z,
                                    outline="black")

        elif instance.get_title() == Pyramid.get_title():
            canvas.create_line(0.9 * (x_centre - instance.get_base()[0]/2),
                               0.9 * (y_centre - instance.get_base()[1]/2),
                               0.9 * (x_centre + instance.get_base()[0] / 2),
                               0.9 * (y_centre - instance.get_base()[1] / 2),
                               x_centre + instance.get_base()[0] / 2,
                               y_centre + instance.get_base()[1] / 2,
                               dash=(5, 5)
                               )
            canvas.create_line(x_centre + instance.get_base()[0] / 2,
                               y_centre + instance.get_base()[1] / 2,
                               x_centre - instance.get_base()[0] / 2,
                               y_centre + instance.get_base()[1] / 2,
                               0.9 * (x_centre - instance.get_base()[0] / 2),
                               0.9 * (y_centre - instance.get_base()[1] / 2),
                               )

            canvas.create_line(x_centre, y_centre - instance.get_height(),
                               0.9 * (x_centre - instance.get_base()[0]/2),
                               0.9 * (y_centre - instance.get_base()[1]/2),)

            canvas.create_line(x_centre, y_centre - instance.get_height(),
                               0.9 * (x_centre + instance.get_base()[0] / 2),
                               0.9 * (y_centre - instance.get_base()[1] / 2), dash=(10, 10))

            canvas.create_line(x_centre, y_centre - instance.get_height(),
                               x_centre + instance.get_base()[0] / 2,
                               y_centre + instance.get_base()[1] / 2, )

            canvas.create_line(x_centre, y_centre - instance.get_height(),
                               x_centre - instance.get_base()[0] / 2,
                               y_centre + instance.get_base()[1] / 2,)

        elif instance.get_title() == Cylinder.get_title():
            canvas.create_arc(x_centre - instance.get_diameter() / 2, y_centre - 20,
                              x_centre + instance.get_diameter() / 2, y_centre + 20,
                              outline="black", start=0, extent=180, )
            canvas.create_arc(x_centre - instance.get_diameter() / 2, y_centre - 20,
                              x_centre + instance.get_diameter() / 2, y_centre + 20,
                              outline="black", start=180, extent=180, )
            canvas.create_arc(x_centre - instance.get_diameter() / 2,
                              y_centre - 20 + instance.get_height(),
                              x_centre + instance.get_diameter() / 2,
                              y_centre + 20 + instance.get_height(),
                              outline="black", start=0, extent=180, dash=(10, 10))
            canvas.create_arc(x_centre - instance.get_diameter() / 2,
                              y_centre - 20 + instance.get_height(),
                              x_centre + instance.get_diameter() / 2,
                              y_centre + 20 + instance.get_height(),
                              outline="black", start=180, extent=180, )
            canvas.create_line(x_centre - instance.get_diameter() / 2,
                               y_centre + instance.get_height(),
                               x_centre - instance.get_diameter() / 2, y_centre)
            canvas.create_line(x_centre + instance.get_diameter() / 2,
                               y_centre + instance.get_height(),
                               x_centre + instance.get_diameter() / 2, y_centre)

        elif instance.get_title() == Sphere.get_title():
            canvas.create_arc(x_centre - instance.get_diameter() / 2,
                              y_centre - instance.get_diameter() / 2,
                              x_centre + instance.get_diameter() / 2,
                              y_centre + instance.get_diameter() / 2,
                              fill="red", outline="black", start=0, extent=180)
            canvas.create_arc(x_centre - instance.get_diameter() / 2,
                              y_centre - instance.get_diameter() / 2,
                              x_centre + instance.get_diameter() / 2,
                              y_centre + instance.get_diameter() / 2,
                              fill="red", outline="black", start=180, extent=180)
            canvas.create_arc(x_centre - instance.get_diameter() / 2, y_centre - 20,
                              x_centre + instance.get_diameter() / 2, y_centre + 20,
                              fill="red", outline="black", start=0, extent=180, dash=(10, 10))
            canvas.create_arc(x_centre - instance.get_diameter() / 2, y_centre - 20,
                              x_centre + instance.get_diameter() / 2, y_centre + 20,
                              fill="red", outline="black", start=180, extent=180)

        else:
            canvas.create_arc(x_centre - instance.get_radius(), y_centre - 20,
                              x_centre + instance.get_radius(), y_centre + 20,
                              outline="black", start=0, extent=180, dash=(10, 10))
            canvas.create_arc(x_centre - instance.get_radius(), y_centre - 20,
                              x_centre + instance.get_radius(), y_centre + 20,
                              outline="black", start=180, extent=180,)
            canvas.create_line(x_centre, y_centre - instance.get_height(), x_centre - instance.get_radius(), y_centre)
            canvas.create_line(x_centre, y_centre - instance.get_height(), x_centre + instance.get_radius(), y_centre)

