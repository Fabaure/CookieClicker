import tkinter as tk
from tkinter import PhotoImage
from Cookie import Cookie
from background import Background


class CookieClickerApp:
    def __init__(self, master):
        self.master = master
        self.background = Background(master)
        self.cookie = Cookie(master)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()
