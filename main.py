import tkinter as tk
from tkinter import PhotoImage
from application import Application
from minijeu1 import Minijeu1



class CookieClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.withdraw()
        self.application = Application(master)
        self.application.Popup()


if __name__ == "__main__":
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()
