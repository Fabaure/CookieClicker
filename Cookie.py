import tkinter as tk
from tkinter import PhotoImage


class Cookie:
    def __init__(self, master, stat_instance, application_instance):
        self.master = master
        self.stat_instance = stat_instance
        self.application_instance = application_instance
        self.image = PhotoImage(file="cookie.png").zoom(2).subsample(4)
        self.cookie_count = 0
        self.cookie_multip = 1
        self.clique = 0
        self.create_widgets()

    def create_widgets(self):
        self.cookie_frame = tk.Frame(self.master, bg="white")
        self.cookie_frame.pack(expand=True)

        self.label_cookie_count = tk.Label(self.cookie_frame, text="Cookie : " + str(self.cookie_count),
                                           font=("Courier", 15), fg="black", bg="white")
        self.label_cookie_count.pack(side="top", pady=20)

        self.cookie_button = tk.Button(self.cookie_frame, image=self.image, bg='white', bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.add_cookie, activebackground="white")
        self.cookie_button.pack()

    def add_cookie(self):
        self.stat_instance.stat_clique += 1
        self.cookie_count += self.cookie_multip
        self.label_cookie_count.config(text="Cookies : " + str(self.cookie_count))
        self.stat_instance.label_clique_nbr.config(text="Nombres de cliques : " + str(self.stat_instance.stat_clique))
        if self.cookie_count >= self.stat_instance.stat_cookie:
            self.refreshcount()

    def refreshcount(self):
        if self.cookie_count >= self.stat_instance.stat_cookie:
            self.stat_instance.stat_cookie = self.cookie_count
            self.master.after(1, self.stat_instance.label_cookie_nbr.config(
                text="Record du nombres de cookie :" + str(self.cookie_count)))

