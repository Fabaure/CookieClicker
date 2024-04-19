import tkinter as tk
from tkinter import PhotoImage
from Cookie import Cookie
from application import Application
from minijeu1 import Minijeu1



class CookieClickerApp:
    def __init__(self, master):
        self.master = master
        self.application = Application(master)


if __name__ == "__main__":
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()
