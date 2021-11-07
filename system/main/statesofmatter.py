# Imports packages
import tkinter as tk
from tkinter import *
import random

# Creates the window
window = tk.Tk()

# Creates a canvas to draw the diagam on
diagramcanvas = Canvas(window, width = 500, height = 400)
diagramcanvas.pack()

# Creates a rectangle
diagramcanvas.create_rectangle(100, 25, 400, 225, outline="#ffffff", fill="#ffffff")

def create_circle(x, y, r, diagramcanvas):
    x0 = x - r # retreives the x value of the top left hand corner
    y0 = y - r # retreives the y value of the top left hand corner
    x1 = x + r # retreives the x value of the bottom right hand corner
    y1 = y + r # retreives the y value of the bottom right hand corner
    return diagramcanvas.create_oval(x0, y0, x1, y1)

create_circle(250, 125, 25, diagramcanvas)

# Loops the window
window.mainloop()
