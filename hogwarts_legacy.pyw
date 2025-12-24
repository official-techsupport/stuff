from tkinter import Tk, Frame

class App(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.winfo_toplevel().title("Hogwarts Legacy (Deluxe Edition)")


root = Tk()
app = App(root)
# root.withdraw()
root.mainloop()
