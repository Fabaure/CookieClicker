import tkinter as tk
from minijeu1 import Minijeu1
from minijeu2 import  Minijeu2
from Cookie import Cookie
from Statistiques import Statistiques


class Minijeu:
    def __init__(self, master, cookie_instance, stat_instance):
        self.master = master
        self.cookie_instance = cookie_instance
        self.stat_instance = stat_instance
        self.create_widgets()
        self.countdown1(5)
        self.countdown2(15)

    def create_widgets(self):
        self.minijeu_frame = tk.Frame(self.master, bg="white")
        self.minijeu_frame.pack(expand=True, side="bottom", padx=10, pady=10)

        self.minijeu_button1 = tk.Button(self.minijeu_frame, text="Mini-jeu n°1\n", anchor="center", command=self.open_minijeu1, height=3, width=50, bg='#E2BFB3')
        self.minijeu_button1.pack(pady=10)

        self.minijeu_button2 = tk.Button(self.minijeu_frame, text="Mini-jeu n°2\n", anchor="center",command=self.open_minijeu2, height=3, width=50, bg='#E2BFB3')
        self.minijeu_button2.pack(pady=30)

    def countdown1(self, count):
        if count > 0:
            self.minijeu_button1.config(text="Mini-jeu n°1\nTemps restant: " + str(count), state="disabled")
            self.master.after(1000, self.countdown1, count - 1)
        else:
            self.minijeu_button1.config(text="Mini-jeu n°1\nDisponible", state="normal")

    def countdown2(self, count):
        if count > 0:
            self.minijeu_button2.config(text="Mini-jeu n°2\nTemps restant: " + str(count), state="disabled")
            self.master.after(1000, self.countdown2, count - 1)
        else:
            self.minijeu_button2.config(text="Mini-jeu n°2\nDisponible", state="normal")
    def open_minijeu1(self):
        minijeu1_window = tk.Toplevel(self.master)
        minijeu1_window.geometry("400x300")
        minijeu1_window.title("Minijeu 1")
        Minijeu1(minijeu1_window, self.cookie_instance, self.stat_instance)
        self.countdown1(5)

    def open_minijeu2(self):
        minijeu2_window = tk.Toplevel(self.master)
        minijeu2_window.geometry("400x300")
        minijeu2_window.title("Minijeu 1")
        Minijeu2(minijeu2_window, self.cookie_instance, self.stat_instance)
        self.countdown2(15)