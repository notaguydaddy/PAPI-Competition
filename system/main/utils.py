from tkinter import *
window = None
class basicOut():
    def __init__(self, window=None): self.window, self.labels = Tk() if not window else window, []
    def printToScreen(self, *s): ((x := Label(self.window, text=' '.join([*s]))).pack(), (self.labels.append(x), self.window.update()))
    def clear(self): [l.destroy() for l in self.labels]
def print(*s):
    global window
    if not window: window = basicOut()
    window.printToScreen(*s)
def clear(): 
    if window: window.clear()