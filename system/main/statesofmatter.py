# Imports packages
import tkinter as tk
from tkinter import *
import random

# Have fun shortening this! :)

coordinatesforliquid, coordinatesforliquid2 = [], []

def create_circle(x, y, r, diagramcanvas):
    x0 = x - r # retreives the x value of the top left hand corner
    y0 = y - r # retreives the y value of the top left hand corner
    x1 = x + r # retreives the x value of the bottom right hand corner
    y1 = y + r # retreives the y value of the bottom right hand corner
    return diagramcanvas.create_oval(x0, y0, x1, y1)

# Creates the window
window = tk.Tk()
window.config()

# Creates a canvas to draw the diagam on
diagramcanvas = Canvas(window, width = 500, height = 400)
diagramcanvas.pack()

decider = 2
if decider == 1:
    # Creates a rectangle
    diagramcanvas.create_rectangle(100, 25, 400, 225, outline="#ffffff", fill="#ffffff")

    # Defines the x and y coordinates of the centre
    xcoordinate, ycoordinate, xcoordinate1, ycoordinate1 = random.randint(105, 325), random.randint(50, 225), random.randint(105, 325), random.randint(50, 225)

    #Blits 2 circles in random coordinates
    create_circle(xcoordinate, ycoordinate, 5, diagramcanvas)
    create_circle(xcoordinate1, ycoordinate1, 5, diagramcanvas)

elif decider == 2:
    diagramcanvas.create_rectangle(100, 25, 400, 225, outline="#ffffff", fill="#ffffff")

    # Blits loads of particles
    for i in range(150):
        xcoordinate, ycoordinate, xcoordinate1, ycoordinate1 = random.randint(105, 400), random.randint(150, 225), random.randint(105, 400), random.randint(150, 225)
        coordinatesforliquid.append(xcoordinate, ycoordinate)
        coordinatesforliquid.append(xcoordinate1, ycoordinate1)
        create_circle(xcoordinate, ycoordinate, 5, diagramcanvas)
        create_circle(xcoordinate1, ycoordinate1, 5, diagramcanvas)
        
# Loops the window
window.mainloop()
