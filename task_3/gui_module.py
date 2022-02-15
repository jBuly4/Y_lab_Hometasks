import tkinter as tk

from flat_figures import Circle, Square, Rectangle, Triangle, Trapezoid, Rhombus

btn_names_main = [class_name.get_title() for class_name in [Circle, Square, Rectangle, Triangle, Trapezoid, Rhombus]]


class MyGUI(tk.Tk):
    count = 0

    def __init__(self):
        super().__init__()
        self.btns = [self.create_btn(text) for text in btn_names_main]

        self.btn_Circle, self.btn_Square, self.btn_Rectangle, \
        self.btn_Triangle, self.btn_Trapezoid, self.Rhombus = self.btns

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

        if text == Circle.get_title():
            method_lst = self.get_lst_methods(Circle)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert radius of {text} ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Square.get_title():
            method_lst = self.get_lst_methods(Square)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side of {text} ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Rectangle.get_title():
            method_lst = self.get_lst_methods(Rectangle)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side 1\n and side 2 of {text}\n with space ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Triangle.get_title():
            method_lst = self.get_lst_methods(Triangle)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side a, b\n and side c of {text}\n with space ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Trapezoid.get_title():
            method_lst = self.get_lst_methods(Trapezoid)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side a, b\n and c, d of {text}\n with space ", width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

        elif text == Rhombus.get_title():
            method_lst = self.get_lst_methods(Rhombus)
            for method in method_lst:
                lb.insert(indx, method)
                indx += 1

            label_sizes = tk.Label(frame_2, text=f"Insert side a\n and one angle in degrees for {text}\n with space ",
                                   width=19)
            label_sizes.pack(side="left", pady=5, padx=5)
            sizes = tk.Entry(frame_2, width=21)
            sizes.pack(fill="x", side="left", pady=5, padx=5)

    def calculate_n_draw(self, event, sizes, text, win):
        x_centre = y_centre = 300 / 2
        canvas_frame = tk.Frame(win)
        canvas_frame.pack()
        canvas = tk.Canvas(canvas_frame)
        canvas.pack(fill="x")

        if text == Circle.get_title():
            try:
                circle = Circle(int(sizes.get()))
                lb_res = tk.Label(win, text=f"Area {circle.get_area()}\nPerimeter {circle.get_perimeter()}\n" \
                                            f"Diameter {circle.get_diameter()}", bg="white")
                lb_res.pack(side="bottom")
                canvas.create_oval(x_centre - circle.get_diameter() / 2, y_centre - circle.get_diameter() / 2, \
                                   x_centre + circle.get_diameter() / 2, y_centre + circle.get_diameter() / 2, \
                                   fill="red", outline="black")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Square.get_title():
            try:
                square = Square(int(sizes.get()))
                lb_res = tk.Label(win, text=f"Area {square.get_area()}\nPerimeter {square.get_perimeter()}\n" \
                                            f"Diagonal {square.get_diagonal()}", bg="white")
                lb_res.pack(side="bottom")
                canvas.create_rectangle(x_centre - square.get_perimeter() / 8, y_centre - square.get_perimeter() / 8, \
                                        x_centre + square.get_perimeter() / 8, y_centre + square.get_perimeter() / 8, \
                                        fill="red", outline="black")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Rectangle.get_title():
            try:
                x, y = map(int, sizes.get().split())
                rectangle = Rectangle(x, y)
                lb_res = tk.Label(win, text=f"Area {rectangle.get_area()}\nPerimeter {rectangle.get_perimeter()}\n" \
                                            f"Diagonal {rectangle.get_diagonal()}", bg="white")
                lb_res.pack(side="bottom")
                canvas.create_rectangle(x_centre - x / 2, y_centre - y / 2, \
                                        x_centre + x / 2, y_centre + y / 2, \
                                        fill="red", outline="black")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Triangle.get_title():
            try:
                a, b, c = map(int, sizes.get().split())
                if not (a + b) >= c and (c + b) >= a and (a + c) >= b:
                    raise ValueError
                triangle = Triangle(a, b, c)
                lb_res = tk.Label(win, text=f"Area {triangle.get_area()}\nPerimeter {triangle.get_perimeter()}\n" \
                                            f"Heigt {triangle.get_height()}", bg="white")
                lb_res.pack(side="bottom")
                canvas.create_line(x_centre - a / 2, y_centre - triangle.get_height(), \
                                   x_centre + a / 2, y_centre - triangle.get_height(), \
                                   x_centre, y_centre, \
                                   x_centre - a / 2, y_centre - triangle.get_height(), \
                                   fill="red")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error or Wrong sides!")
                lb_err.pack()

        elif text == Trapezoid.get_title():
            try:
                a, b, c, d = map(int, sizes.get().split())
                trapezoid = Trapezoid(a, b, c, d)
                lb_res = tk.Label(win, text=f"Area {trapezoid.get_area()}\nPerimeter {trapezoid.get_perimeter()}\n" \
                                            f"Heigt {trapezoid.get_height()}", bg="white")
                lb_res.pack(side="bottom")
                canvas.create_line(x_centre - a / 2, y_centre - trapezoid.get_height(), \
                                   x_centre + a / 2, y_centre - trapezoid.get_height(), \
                                   x_centre + b / 2, y_centre, \
                                   x_centre - b / 2, y_centre, \
                                   x_centre - a / 2, y_centre - trapezoid.get_height(), \
                                   fill="red")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

        elif text == Rhombus.get_title():
            try:
                a, angle = map(int, sizes.get().split())
                rhomb = Rhombus(a, angle)
                lb_res = tk.Label(win, text=f"Area {rhomb.get_area()}\nPerimeter {rhomb.get_perimeter()}\n" \
                                            f"Diagonals {rhomb.get_diagonals()}", bg="white")
                lb_res.pack(side="bottom")
                d1, d2 = rhomb.get_diagonals()
                canvas.create_line(x_centre - d2 / 2, y_centre, \
                                   x_centre, y_centre - d1 / 2, \
                                   x_centre + d2 / 2, y_centre, \
                                   x_centre, y_centre + d1 / 2, \
                                   x_centre - d2 / 2, y_centre, \
                                   fill="red")
            except ValueError:
                lb_err = tk.Label(win, text=f"Value Error!")
                lb_err.pack()

    def get_lst_methods(self, class_name):
        return [method for method in dir(class_name) if not method.startswith('__')]


app = MyGUI()
app.title("Geometric calculator")
app.mainloop()
