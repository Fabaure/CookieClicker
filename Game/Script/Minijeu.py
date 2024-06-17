# Importation de classes et de modules
import tkinter as tk
from minijeu1 import Minijeu1
from minijeu2 import Minijeu2
from minijeu3 import Minijeu3
from tkinter import PhotoImage  # Gestion d'images

class Minijeu:
    def __init__(self, master, cookie_instance, stat_instance, application_instance):
        self.master = master
        self.cookie_instance = cookie_instance  # Instance gérant les cookies
        self.stat_instance = stat_instance  # Instance gérant les statistiques
        self.application_instance = application_instance  # Instance principale de l'application

        # Conditions pour débloquer les mini-jeux (en nombre de cookies requis)
        self.minijeu1 = 500
        self.minijeu2 = 10000
        self.minijeu3 = 50000

        # Vérifier l'état des mini-jeux
        self.check_minijeu()

        # Créer les widgets de l'interface graphique
        self.create_widgets()

    def create_widgets(self):
        # Création d'un cadre pour les mini-jeux
        self.minijeu_frame = tk.Frame(self.master, bg=self.application_instance.bg_main)
        self.minijeu_frame.pack(expand=True)

        # Bouton pour le mini-jeu n°1
        self.minijeu_button1 = tk.Button(self.minijeu_frame, text="Mini-jeu n°1\nAtteindre 500 cookies pour le débloquer", anchor="center", command=self.open_minijeu1, height=3, width=50, bg="#F1C8E1", state="disabled")
        self.minijeu_button1.pack(pady=20)

        # Bouton pour le mini-jeu n°2
        self.minijeu_button2 = tk.Button(self.minijeu_frame, text="Mini-jeu n°2\nAtteindre 10 000 cookies pour le débloquer", anchor="center",command=self.open_minijeu2, height=3, width=50, bg="#F1C8E1", state="disabled")
        self.minijeu_button2.pack(pady=20)

        # Bouton pour le mini-jeu n°3
        self.minijeu_button3= tk.Button(self.minijeu_frame, text="Mini-jeu n°3\nAtteindre 50 0000 cookies pour le débloquer", anchor="center", command=self.open_minijeu3, height=3, width=50, bg="#F1C8E1", state="disabled")
        self.minijeu_button3.pack(pady=20)

        # Bouton pour activer tous les mini-jeux (démonstration)
        self.star = PhotoImage(file="Assets/Images/magical_star.png").subsample(3,3)
        self.magical_button = tk.Button(self.minijeu_frame, image=self.star, bg=self.application_instance.bg_main, bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.activate_all, activebackground=self.application_instance.bg_main)
        self.magical_button.pack()

    def check_minijeu(self):
        # Vérifier si les conditions pour débloquer les mini-jeux sont remplies
        if self.cookie_instance.cookie_count >= self.minijeu1 and self.minijeu1 != 0:
            message = "Le mini jeu 1 est débloqué\n\nRendez-vous dans la page Mini jeu pour pouvoir y jouer dès maintenant !"
            self.application_instance.display_message(message)
            self.countdown1(0)  # Démarrer le compte à rebours pour le mini-jeu 1
            self.minijeu1 = 0  # Marquer le mini-jeu 1 comme débloqué
            self.master.after(1000, self.check_minijeu)  # Vérifier périodiquement l'état des mini-jeux
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
        else:
            self.master.after(1000, self.check_minijeu)

    def countdown1(self, count):
        # Compte à rebours pour le mini-jeu 1
        if count > 0:
            self.minijeu_button1.config(text="Mini-jeu n°1\nTemps restant: " + str(count) + " secondes",
                                        state="disabled")
            self.master.after(1000, self.countdown1, count - 1)
        else:
            self.minijeu_button1.config(text="Mini-jeu n°1\nDisponible", state="normal")

    def countdown2(self, count):
        # Compte à rebours pour le mini-jeu 2
        if count > 0:
            self.minijeu_button2.config(text="Mini-jeu n°2\nTemps restant: " + str(count) + " secondes",
                                        state="disabled")
            self.master.after(1000, self.countdown2, count - 1)
        else:
            self.minijeu_button2.config(text="Mini-jeu n°2\nDisponible", state="normal")

    def countdown3(self, count):
        # Compte à rebours pour le mini-jeu 3
        if count > 0:
            self.minijeu_button3.config(text="Mini-jeu n°3\nTemps restant: " + str(count) + " secondes",
                                        state="disabled")
            self.master.after(1000, self.countdown3, count - 1)
        else:
            self.minijeu_button3.config(text="Mini-jeu n°3\nDisponible", state="normal")

    def open_minijeu1(self):
        # Fonction pour ouvrir le mini-jeu 1 dans une nouvelle fenêtre
        minijeu1_window = tk.Toplevel(self.master)
        minijeu1_window.geometry("400x300")
        minijeu1_window.title("Minijeu 1")
        Minijeu1(minijeu1_window, self.cookie_instance, self.stat_instance)
        self.countdown1(300)  # Démarrer le compte à rebours pour le mini-jeu 1

    def open_minijeu2(self):
        # Fonction pour ouvrir le mini-jeu 2 dans une nouvelle fenêtre
        minijeu2_window = tk.Toplevel(self.master)
        minijeu2_window.geometry("400x300")
        minijeu2_window.title("Minijeu 2")
        Minijeu2(minijeu2_window, self.stat_instance, self.cookie_instance)
        self.countdown2(600)

    def open_minijeu3(self):
        # Fonction pour ouvrir le mini-jeu 3 dans une nouvelle fenêtre
        minijeu3_window = tk.Toplevel(self.master)
        minijeu3_window.geometry("400x300")
        minijeu3_window.title("Minijeu 3")
        Minijeu3(minijeu3_window, self.stat_instance, self.cookie_instance)
        self.countdown3(900)

    def activate_all(self):
        # Fonction pour activer tous les mini-jeux (démonstration, à enlever après)
        self.minijeu_button1.config(state="normal")
        self.minijeu_button2.config(state="normal")
        self.minijeu_button3.config(state="normal")
