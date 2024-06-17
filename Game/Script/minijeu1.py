# Importation de modules
import tkinter as tk
from tkinter import PhotoImage  # Gestion des images
from math import *

class Minijeu1:
    def __init__(self, master, cookie_instance, stat_instance):
        # Initialisation de la classe Minijeu1 avec plusieurs instances et paramètres
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.master.title("Cookie Clicker")
        self.master.geometry("600x600")
        self.game_started = False
        self.create_widgets()  # Appel de la méthode pour créer les widgets
        # Initiation des paramètres
        self.cookie_reward = 0
        self.cookies = 0


    def create_widgets(self):
        # Création des widgets de l'interface
        self.background_image = PhotoImage(file="Assets/Images/fond.png")  # Image de fond
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        side_frame = tk.Frame(self.master, bg='#FEDCE4')  # Création d'un cadre pour afficher les règles
        side_frame.place(relx=0.5, rely=0.05, anchor='n')

        rules_text = ("Bonjour et bienvenue à notre premier mini-jeu !\n Dans celui-ci, la rapidité est la clé, alors soyez vif et ne vous trompez pas. "
                      "\n Vous disposez de trente secondes pour cliquer autant de fois que possible sur le cookie. "
                      "\n Dépêchez-vous et tentez de décrocher les meilleures récompenses ! "
                      "\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center", bg='#FEDCE4')  # Création d'un label avec les règles du jeu
        rules_label.pack(pady=20)

        self.cookies_label = tk.Label(self.master, text="Cookies: 0", bg='#FEDCE4')  # Création d'un label pour afficher le nombre de cookies
        self.cookies_label.place(relx=0.5, rely=0.25, anchor='n')

        self.cookie_image = PhotoImage(file="Assets/Images/cookie.png").subsample(3, 3)  # Chargement de l'image du cookie et redimensionnement
        self.cookie_button = tk.Button(self.master, image=self.cookie_image, command=self.click_cookie, state="disabled", borderwidth=0, bg='#FEDCE4', activebackground="#FEDCE4")
        self.cookie_button.place(relx=0.5, rely=0.55, anchor='center')

        self.start_image = PhotoImage(file="Assets/Images/bouton.png").subsample(3, 3)  # Chargement de l'image du bouton Start et redimensionnement
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0, bg='#FEDCE4', activebackground="#FEDCE4")
        self.start_button.place(relx=0.5, rely=0.80, anchor='center')

        self.timer_label = tk.Label(self.master, bg='#FEDCE4')  # Création d'un label pour afficher le temps restant

    def click_cookie(self):
        # Méthode appelée lorsqu'on clique sur le cookie
        if self.game_started:
            self.cookies += 1
            self.cookies_label.config(text="Cookies: " + str(self.cookies))

    def start_game(self):
        # Méthode appelée pour démarrer le jeu
        if not self.game_started:
            self.game_started = True
            self.cookies = 0  # Réinitialisation du nombre de cookies
            self.cookies_label.config(text="Cookies: 0")
            self.start_button.place_forget()  # Cacher le bouton Start
            self.timer_label.place(relx=0.5, rely=0.85, anchor='center')  # Placement du label du timer
            self.cookie_button.config(state="normal")  # Activer le bouton du cookie
            self.countdown(30)  # Démarrer le compte à rebours de 30 secondes

    def countdown(self, count):
        # Méthode de compte à rebours
        if count > 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.show_reward()  # Afficher la récompense
            self.record()  # Enregistrer le record
            self.end_game()  # Terminer le jeu

    def show_reward(self):
        # Méthode pour afficher la récompense en fonction du nombre de cookies obtenus
        if self.cookies >= 300:
            self.cookie_reward = 5000 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau expert ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.cookies >= 200:
            self.cookie_reward = 1000 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau intermédiaire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.cookies >= 100:
            self.cookie_reward = 500 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau débutant ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        else:
            self.cookie_reward = 100 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous pouvez mieux faire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        reward_label = tk.Label(self.master, text=reward, bg='#FEDCE4')
        reward_label.place(relx=0.5, rely=0.9, anchor='center')
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
    def record(self):
        # Méthode pour enregistrer le record du mini-jeu
        if self.cookies >= self.stat_instance.record_mn1:
            self.stat_instance.record_mn1 = self.cookies
            self.stat_instance.label_record_mn1.config(text="Record du mini-jeu 1 : " + str(self.stat_instance.record_mn1) + " Cookies")

    def end_game(self):
        # Méthode pour terminer le jeu
        self.game_started = False
        self.cookie_button.config(state="disabled")  # Désactiver le bouton du cookie
        self.start_button.place_forget()  # Cacher le bouton Start
        self.timer_label.place_forget()  # Cacher le label du timer
