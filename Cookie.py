import tkinter as tk
from tkinter import PhotoImage


class Cookie:
    def __init__(self, master):
        self.master = master
        self.image = PhotoImage(file="cookie.png").zoom(2).subsample(4)
        self.cookie_count = 0
        self.cookie_multip = 1
        self.create_widgets()

    def create_widgets(self):
        self.cookie_frame = tk.Frame(self.master, bg="white")
        self.cookie_frame.pack(expand=True)

        self.label_cookie_count = tk.Label(self.cookie_frame, text="Cookie : " + str(self.cookie_count), font=("Courier", 15), fg="black", bg="white")
        self.label_cookie_count.pack(side="top", pady=20)

        self.cookie_button = tk.Button(self.cookie_frame, image=self.image, bg='white', bd=0, relief=tk.SUNKEN, highlightthickness=0, command=self.add_cookie, activebackground="white")
        self.cookie_button.pack()

    def add_cookie(self):
        self.cookie_count += self.cookie_multip
        self.label_cookie_count.config(text="Cookies : " + str(self.cookie_count))

