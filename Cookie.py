import tkinter as tk
from tkinter import PhotoImage

class Cookie:
    def __init__(self, master):
        self.master = master
        self.image = PhotoImage(file="cookie.png").zoom(8).subsample(32)
        self.cookie_count = 0

        self.label_counter = tk.Label(self.master, text=self.cookie_count, font=("Courier", 30), bg="#5886e7")
        self.label_counter.grid(row=0, column=0, pady=20, padx=20)

        self.button = tk.Button(self.master, image=self.image, bg='#5886e7', bd=0, relief=tk.SUNKEN, highlightthickness=0, command=self.add_cookie,  activebackground="#5886e7")
        self.button.grid(row=1, column=0, pady=20, padx=20)

    def add_cookie(self):
        self.cookie_count += 1
        self.label_counter.config(text=self.cookie_count)