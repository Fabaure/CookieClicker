import tkinter as tk
from minijeu1 import Minijeu1

class Minijeu:
    def __init__(self, master):
        self.master = master
        self.temps1 = 0
        self.temps2 = 0
        self.temps3 = 0
        self.timer_label = tk.Label(self.master, text="")
        self.create_widgets()
        self.countdown1(5)

    def create_widgets(self):
        self.minijeu_frame = tk.Frame(self.master, bg="white")
        self.minijeu_frame.pack(expand=True, side="bottom", padx=10, pady=10)

        self.minijeu_button1 = tk.Button(self.minijeu_frame, text="Mini-jeu n°1\n", anchor="center", command=self.open_minijeu1, height=3, width=50, bg='#E2BFB3')
        self.minijeu_button1.pack(pady=10)

    def countdown1(self, count):
        if count > 0:
            self.minijeu_button1.config(text="Mini-jeu n°1\nTemps restant: " + str(count), state="disabled")
            self.master.after(1000, self.countdown1, count - 1)
        else:
            self.minijeu_button1.config(text="Mini-jeu n°1\nDisponible", state="normal")
    def open_minijeu1(self):
        minijeu_window = tk.Toplevel(self.master)
        minijeu_window.geometry("400x300")
        minijeu_window.title("Minijeu 1")
        Minijeu1(minijeu_window)
        self.countdown1(5)
