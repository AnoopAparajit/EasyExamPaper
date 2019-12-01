import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.LeftFrame = tk.Frame()
        LeftFrame = self.LeftFrame
        LeftFrame.pack(side="left")
        LeftFrame.hi_there = tk.Button(LeftFrame)
        LeftFrame.hi_there["text"] = "Hello World\n(click me)"
        LeftFrame.hi_there["command"] = self.say_hi
        LeftFrame.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.state('zoomed')
app = Application(master=root)
app.mainloop()