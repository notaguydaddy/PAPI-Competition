from tkinter import *
window = None
class basicOut():
    def __init__(self, window=None): self.window, self.items = Tk() if not window else window, []
    def printToScreen(self, *s): ((x := Label(self.window, text=' '.join([*s]))).pack(), (self.items.append(x), self.window.update()))
    def clear(self, items=None, fromTop=True):
        items = len(self.items) if not items else items
        a, b = (0, items) if fromTop else (items+1, len(self.items))
        [l.destroy() for l in self.items[a:b]] # Add ability to clear from top, bottom, or all
        del self.items[a:b]
        self.window.update()
    def input(self, *s):
        if len(s) > 0: self.printToScreen(*s)
        (entry := Entry(self.window)).pack()
        wait_var = IntVar()
        (button := Button(self.window, text="Enter", command=lambda: wait_var.set(1))).pack()
        self.window.update()
        [self.items.append(x) for x in [entry, button]]
        while not (x := entry.get()): button.wait_variable(wait_var)
        return x
    
def print(*s):
    global window
    if not window: window = basicOut()
    window.printToScreen(*s)
    
def clear(items=None, top=True): 
    if window: window.clear(items, top)

def input(*s):
    global window
    if not window: window = basicOut()
    return window.input(*s)