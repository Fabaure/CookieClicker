import tkinter as tk
from minijeu1 import Minijeu1
from minijeu2 import  Minijeu2
from minijeu3 import Minijeu3
from tkinter import PhotoImage

class Minijeu:
    def __init__(self, master, cookie_instance, stat_instance, application_instance):
        self.master = master
        self.cookie_instance = cookie_instance
        self.stat_instance = stat_instance
        self.application_instance = application_instance

        self.minijeu1 = 500
        self.minijeu2 = 10000
        self.minijeu3 = 50000

        self.check_minijeu()
        self.create_widgets()

    def create_widgets(self):
        self.minijeu_frame = tk.Frame(self.master, bg="white")
        self.minijeu_frame.pack(expand=True, side="bottom", padx=10, pady=10)

        self.minijeu_button1 = tk.Button(self.minijeu_frame, text="Mini-jeu n°1\nAtteindre 500 cookies pour le débloquer", anchor="center", command=self.open_minijeu1, height=3, width=50, bg='#E2BFB3', state="disabled")
        self.minijeu_button1.pack(pady=20)

        self.minijeu_button2 = tk.Button(self.minijeu_frame, text="Mini-jeu n°2\nAtteindre 10 000 cookies pour le débloquer", anchor="center",command=self.open_minijeu2, height=3, width=50, bg='#E2BFB3', state="disabled")
        self.minijeu_button2.pack(pady=20)

        self.minijeu_button3= tk.Button(self.minijeu_frame, text="Mini-jeu n°3\nAtteindre 50 0000 cookies pour le débloquer", anchor="center", command=self.open_minijeu3, height=3, width=50, bg='#E2BFB3', state="disabled")
        self.minijeu_button3.pack(pady=20)

        self.star = PhotoImage(file="magical_star.png").subsample(3,3)
        self.magical_button = tk.Button(self.minijeu_frame, image=self.star, bg='white', bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.activate_all, activebackground="white")
        self.magical_button.pack()

    def check_minijeu(self):
        if self.cookie_instance.cookie_count >= self.minijeu1 and self.minijeu1 != 0:
            message = "Le mini jeu 1 est débloqué\n\nRendez-vous dans la page Mini jeu pour pouvoir y jouer dès maintenant !"
            self.application_instance.display_message(message)
            self.countdown1(0)
            self.minijeu1 = 0
            self.master.after(1000, self.check_minijeu)
        elif self.cookie_instance.cookie_count >= self.minijeu2 and self.minijeu2 != 0:
            message = "Le mini jeu 2 est débloqué\n\nRendez-vous dans la page Mini jeu pour pouvoir y jouer dès maintenant !\n\n Vous avez débloqué l'avatar 1!\n\nRendez-vous dans la page Boutique pour pouvoir le tester!"
            self.application_instance.display_message(message)
            self.countdown2(0)
            self.minijeu2 = 0
            self.master.after(1000, self.check_minijeu)
        elif self.cookie_instance.cookie_count >= self.minijeu3 and self.minijeu3 != 0:
            message = "Le mini jeu 3 est débloqué\n\nRendez-vous dans la page Mini jeu pour pouvoir y jouer dès maintenant !\n\n Vous avez débloqué l'avatar 2!\n\nRendez-vous dans la page Boutique pour pouvoir le tester!"
            self.application_instance.display_message(message)
            self.countdown3(0)
            self.minijeu3 = 0
        else :
            self.master.after(1000, self.check_minijeu)

    def countdown1(self, count):
        if count > 0:
            self.minijeu_button1.config(text="Mini-jeu n°1\nTemps restant: " + str(count) + " secondes", state="disabled")
            self.master.after(1000, self.countdown1, count - 1)
        else:
            self.minijeu_button1.config(text="Mini-jeu n°1\nDisponible", state="normal")

    def countdown2(self, count):
        if count > 0:
            self.minijeu_button2.config(text="Mini-jeu n°2\nTemps restant: " + str(count) + " secondes", state="disabled")
            self.master.after(1000, self.countdown2, count - 1)
        else:
            self.minijeu_button2.config(text="Mini-jeu n°2\nDisponible", state="normal")

    def countdown3(self, count):
        if count > 0:
            self.minijeu_button3.config(text="Mini-jeu n°3\nTemps restant: " + str(count) + " secondes", state="disabled")
            self.master.after(1000, self.countdown3, count - 1)
        else:
            self.minijeu_button3.config(text="Mini-jeu n°3\nDisponible", state="normal")


    def open_minijeu1(self):
        minijeu1_window = tk.Toplevel(self.master)
        minijeu1_window.geometry("400x300")
        minijeu1_window.title("Minijeu 1")
        Minijeu1(minijeu1_window, self.cookie_instance, self.stat_instance)
        self.countdown1(300)

    def open_minijeu2(self):
        minijeu2_window = tk.Toplevel(self.master)
        minijeu2_window.geometry("400x300")
        minijeu2_window.title("Minijeu 2")
        Minijeu2(minijeu2_window, self.stat_instance, self.cookie_instance)
        self.countdown2(600)

    def open_minijeu3(self):
        minijeu3_window = tk.Toplevel(self.master)
        minijeu3_window.geometry("400x300")
        minijeu3_window.title("Minijeu 3")
        Minijeu3(minijeu3_window, self.stat_instance, self.cookie_instance)
        self.countdown3(900)

    # fonction pour demo prof (à enlever après)
    def activate_all(self):
        self.minijeu_button1.config(state="normal")
        self.minijeu_button2.config(state="normal")
        self.minijeu_button3.config(state="normal")
