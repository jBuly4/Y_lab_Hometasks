import tkinter as tk
from tkinter import messagebox
from D_gui_module import My_3D_GUI
from gui_module import MyGUI


def start_calc(root, text):
    if text == "flat":
        app = MyGUI()
        app.title("Geometric calculator for flat figures")
        # app.mainloop()
    else:
        app = My_3D_GUI()
        app.title("Geometric calculator for 3D figures")
        # app.mainloop()


def main():
    root = tk.Tk()
    root.title("Welcome to geometric calculator")
    root.geometry("300x100")

    btn1 = tk.Button(root, text="Flat figures", command=lambda x="flat": start_calc(root, x))
    btn1.pack(fill="x")

    btn2 = tk.Button(root, text="3D figures", command=lambda x="3D": start_calc(root, x))
    btn2.pack(fill="x")

    status_bar = tk.Label(root, relief="sunken", anchor="center", text="Geometric calculator, v.0.1")
    status_bar.pack(side="bottom", fill="x")

    root.mainloop()


if __name__ == "__main__":
    main()


