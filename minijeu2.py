# Importation de modules
import tkinter as tk
from tkinter import PhotoImage  # Gestion d'images
from math import ceil

class Minijeu2:
    def __init__(self, master, stat_instance, cookie_instance):
        # Initialisation de la classe Minijeu2 avec plusieurs instances et paramètres
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.master.title("Sauve ton cookie!")
        self.master.geometry("600x600")

        self.cookie_reward = 0
        self.game_started = False

        #Initialisation des compteurs à 0
        self.monstre_niveau1_clicks = 0
        self.monstre_niveau2_clicks = 0
        self.monstre_niveau3_clicks = 0
        self.level = 0

        self.create_widgets()  # Appel de la méthode pour créer les widgets

    def create_widgets(self):
        # Création des widgets de l'interface
        self.background_image = PhotoImage(file="fond2.png")
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        side_frame = tk.Frame(self.master, bg='#FAEFD6')
        side_frame.place(relx=0.5, rely=0.05, anchor='n')

        rules_text = ("Bonjour et bienvenue à notre deuxième mini-jeu !"
                      "\n Dans celui-ci, la rapidité est la clé, alors soyez vif. "
                      "\n Défendez votre cookie de macaron le glouton en cliquant sur lui lorsqu'il apparait. "
                      "\n Appuyez plusieurs fois jusqu'à ce qu'il disparaisse "
                      "\n Attention il est de plus en plus énervé, franchi les 3 niveaux"
                      "\n Si vous n'arrivez pas à battre macaron le glouton à temps vous avez perdu"
                      "\n Tentez de décrocher les meilleures récompenses ! "
                      "\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center", bg='#FAEFD6')  # Création d'un label avec les règles du jeu
        rules_label.pack(pady=20)

        self.niveau_label = tk.Label(self.master, text="Niveau: 0", bg='#FAEFD6')  # Création d'un label pour afficher le niveau
        self.niveau_label.place(relx=0.5, rely=0.35, anchor='n')

        self.cookie_image = PhotoImage(file="cookie.png").subsample(3, 3)  # Chargement de l'image du cookie et redimensionnement
        self.cookie_label = tk.Label(self.master, image=self.cookie_image, borderwidth=0, bg='#FAEFD6', activebackground='#FAEFD6')
        self.cookie_label.place(relx=0.2, rely=0.59, anchor='center')

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)  # Chargement de l'image du bouton Start et redimensionnement
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0, bg='#FAEFD6', activebackground='#FAEFD6')
        self.start_button.place(relx=0.5, rely=0.9, anchor='center')

        self.timer_label = tk.Label(self.master, bg='#FAEFD6')  # Création d'un label pour afficher le temps restant

    def start_game(self):
        # Méthode appelée pour démarrer le jeu
        if not self.game_started:
            self.game_started = True
            self.cookies = 0
            self.niveau_label.config(text="Niveau: 1")
            self.start_button.place_forget()
            self.timer_label.place(relx=0.5, rely=0.85, anchor='center')
            self.countdown(60)  # Démarrer le compte à rebours de 60 secondes
            self.monstre_niveau1()  # Démarrer le premier niveau du monstre

    def countdown(self, count):
        # Méthode de compte à rebours
        if count >= 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            if self.game_started:
                self.end_game()

    def monstre_niveau1(self):
        # Méthode pour afficher le monstre du niveau 1
        self.monstre_image = PhotoImage(file="monstrecontent.png").subsample(4, 4)  # Chargement de l'image du monstre et redimensionnement
        self.monstre_button = tk.Button(self.master, image=self.monstre_image, command=self.monstre_action, borderwidth=0, bg='#FAEFD6', activebackground='#FAEFD6')
        self.monstre_button.place(relx=0.8, rely=0.59, anchor='center')

    def monstre_action(self):
        # Méthode appelée lorsqu'on clique sur le monstre du niveau 1
        self.monstre_niveau1_clicks += 1
        if self.monstre_niveau1_clicks == 100:
            self.level += 1  # Incrémentation du niveau
            self.monstre_button.place_forget()  # Cacher le bouton du monstre
            self.monstre_niveau2()  # Démarrer le deuxième niveau du monstre

    def monstre_niveau2(self):
        # Méthode pour afficher le monstre du niveau 2
        self.monstre_niveau2_image = PhotoImage(file="monstredecu.png").subsample(2, 2)
        self.monstre_niveau2_button = tk.Button(self.master, image=self.monstre_niveau2_image, command=self.monstre_niveau2_action, borderwidth=0, bg='#FAEFD6', activebackground='#FAEFD6')
        self.monstre_niveau2_button.place(relx=0.7, rely=0.59, anchor='center')

    def monstre_niveau2_action(self):
        # Méthode appelée lorsqu'on clique sur le monstre du niveau 2
        self.niveau_label.config(text="Niveau: 2")
        self.monstre_niveau2_clicks += 1
        if self.monstre_niveau2_clicks == 150:
            self.level += 1
            self.monstre_niveau2_button.place_forget()
            self.monstre_niveau3()  # Démarrer le troisième niveau du monstre

    def monstre_niveau3(self):
        # Méthode pour afficher le monstre du niveau 3
        self.monstre_niveau3_image = PhotoImage(file="monstreenerve.png").subsample(2, 2)
        self.monstre_niveau3_button = tk.Button(self.master, image=self.monstre_niveau3_image, command=self.monstre_niveau3_action, borderwidth=0, bg='#FAEFD6', activebackground='#FAEFD6')
        self.monstre_niveau3_button.place(relx=0.6, rely=0.59, anchor='center')
    def monstre_niveau3_action(self):
        # Méthode appelée lorsqu'on clique sur le monstre du niveau 3
        self.niveau_label.config(text="Niveau: 3")
        self.monstre_niveau3_clicks += 1
        if self.monstre_niveau3_clicks == 200:
            self.level += 1
            self.end_game()  # Terminer le jeu

    def show_reward(self):
        # Méthode pour afficher la récompense en fonction du niveau atteint
        if self.level == 3:
            self.monstre_niveau3_button.place_forget()
            self.center_cookie()
            self.cookie_reward = 7500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau expert ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.level == 2:
            self.monstre_niveau3_button.place_forget()
            self.cookie_reward = 2500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau intermédiaire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
            self.monstre_perdu()  # Afficher l'image du monstre qui a gagné
        elif self.level == 1:
            self.monstre_niveau2_button.place_forget()
            self.cookie_reward = 750 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau débutant ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
            self.monstre_perdu()
        else:
            self.monstre_button.place_forget()
            self.cookie_reward = 250 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous pouvez mieux faire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
            self.monstre_perdu()

        reward_label = tk.Label(self.master, text=reward, bg='#FAEFD6')  # Création d'un label pour afficher la récompense
        reward_label.place(relx=0.5, rely=0.9, anchor='center')
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))  # Mise à jour du label du nombre de cookies

    def record(self):
        # Méthode pour enregistrer le record si le nombre de cookies est supérieur au record actuel
        if self.cookies >= self.stat_instance.record_mn2:
            self.stat_instance.record_mn2 = self.cookie_reward
            self.stat_instance.label_record_mn2.config(text="Record du mini-jeu 2 : " + str(self.stat_instance.record_mn2) + " Cookies")

    def monstre_perdu(self):
        # Méthode pour afficher l'image du monstre qui a gagné
        self.cookie_label.place_forget()
        self.monstre_perdu_image = PhotoImage(file="monstreaveccookie.png").subsample(2, 2)
        self.monstre_perdu_label = tk.Label(self.master, image=self.monstre_perdu_image, borderwidth=0, bg='#FAEFD6')
        self.monstre_perdu_label.place(relx=0.5, rely=0.65, anchor='center')

    def center_cookie(self):
        # Méthode pour centrer le cookie
        self.cookie_label.place_forget()
        self.cookie_label.place(relx=0.5, rely=0.6, anchor='center')

    def end_game(self):
        # Méthode pour terminer le jeu
        self.show_reward()  # Afficher la récompense
        self.record()  # Enregistrer le record
        self.game_started = False
        self.start_button.place_forget()
        self.timer_label.place_forget()
