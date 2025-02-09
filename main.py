from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        root = Tk()
        root.title("My Title")
        canvas = Canvas()
