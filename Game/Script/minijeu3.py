# Importation de modules
import tkinter as tk
from tkinter import PhotoImage  # Gestion d'images
from math import *
import random

class Minijeu3:
    def __init__(self, master, stat_instance, cookie_instance):
        # Initialisation de la classe Minijeu3 avec plusieurs instances et paramètres
        self.master = master
        self.master.title("Mange pépites!")
        self.master.geometry("900x600")
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.game_started = False
        # Initialisation compteurs à 0
        self.choco = 0
        self.level = 0
        self.create_widgets()  # Appel de la méthode pour créer les widgets

    def create_widgets(self):
        # Création des widgets de l'interface
        self.background_image = PhotoImage(file="Assets/Images/background.png")
        self.background_label = tk.Label(self.master, image=self.background_image)  # Création d'un label avec l'image de fond
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        side_frame = tk.Frame(self.master, bg='#D3E6FF')  # Création d'un cadre pour afficher les règles
        side_frame.place(relx=0.5, rely=0.05, anchor="n", width=880, height=150)

        rules_text = ("Bonjour et bienvenue à notre troisième mini-jeu !\n Dans celui-ci, la rapidité est la clé, alors soyez vif et précis!"
                      "\n Vous disposez d'une minute pour cliquer sur toutes les pépites de chocolat qui apparaissent sur le cookie"
                      "\n Dans ce jeu, vous trouverez plusieurs niveaux qui montent en difficulté."
                      "\n Régalez-vous et tentez de décrocher les meilleures récompenses ! "
                      "\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center", bg='#D3E6FF')  # Création d'un label avec les règles du jeu
        rules_label.place(relx=0.5, rely=0.5, anchor="center")

        self.choco_label = tk.Label(self.master, text="Pépites: 0", bg='#D3E6FF')  # Création d'un label pour afficher le nombre de pépites
        self.choco_label.place(relx=0.5, rely=0.3, anchor="center")

        self.niveau_label = tk.Label(self.master, text="Niveau: 0", bg='#D3E6FF')  # Création d'un label pour afficher le niveau
        self.niveau_label.place(relx=0.5, rely=0.35, anchor="center")

        self.cookie_image = PhotoImage(file="Assets/Images/cookie_sans_pepite.png").subsample(2, 2)  # Chargement de l'image du cookie et redimensionnement

        self.cookie_canvas = tk.Canvas(self.master, width=255, height=225, highlightthickness=0, bg='#D3E6FF')  # Création d'un canvas pour afficher le cookie
        self.cookie_canvas.place(relx=0.5, rely=0.6, anchor="center")
        self.cookie_canvas.create_image(0, 0, anchor=tk.NW, image=self.cookie_image)

        self.start_image = PhotoImage(file="Assets/Images/bouton.png").subsample(3, 3)  # Chargement de l'image du bouton Start et redimensionnement
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0, bg='#D3E6FF', activebackground='#D3E6FF')
        self.start_button.place(relx=0.5, rely=0.87, anchor="center")

        self.timer_label = tk.Label(self.master, bg='#D3E6FF')  # Création d'un label pour afficher le temps restant

    def start_game(self):
        # Méthode appelée pour démarrer le jeu
        if not self.game_started:
            self.game_started = True
            self.level = 0
            self.choco = 0
            self.niveau_label.config(text="Niveau: 0")
            self.choco_label.config(text="Pépites: 0")
            self.start_button.place_forget()
            self.timer_label.place(relx=0.5, rely=0.85, anchor="center")
            self.countdown(30)  # Démarrer le compte à rebours de 30 secondes
            self.niveau1()  # Démarrer le premier niveau

    def create_multiple_chocolates(self, num_chocolates):
        # Méthode pour créer plusieurs pépites de chocolat
        self.clear_chocolates()  # Nettoyage des pépites existantes
        self.chocolates = []
        for _ in range(num_chocolates):  # Création du nombre de pépites donné
            chocolate_id = self.create_chocolate()  # Création d'une pépite de chocolat
            self.chocolates.append(chocolate_id)
            self.cookie_canvas.tag_bind(chocolate_id, "<Button-1>", self.click_chocolate)

    def create_chocolate(self):
        # Méthode pour créer une pépite de chocolat à une position aléatoire
        x = random.randint(50, 200)
        y = random.randint(50, 150)
        return self.cookie_canvas.create_oval(x, y, x + 20, y + 20, fill="#7C473B", outline="")  # Création de la pépite

    def click_chocolate(self, event):
        # Méthode appelée lorsqu'on clique sur une pépite de chocolat
        self.choco += 1
        self.choco_label.config(text="Pépites: " + str(self.choco))
        self.cookie_canvas.delete(tk.CURRENT)  # Suppression de la pépite cliquée
        if self.choco == 5:
            self.niveau2()
        elif self.choco == 15:
            self.niveau3()
        elif self.choco == 30:
            self.end_game()

    def countdown(self, count):
        # Méthode de compte à rebours
        if count > 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.end_game()

    def clear_chocolates(self):
        # Méthode pour enlever les pépites de chocolat du canvas
        self.cookie_canvas.delete("all")  # Suppression de tous les éléments du canvas
        self.cookie_canvas.create_image(0, 0, anchor=tk.NW, image=self.cookie_image)

    def niveau1(self):
        # Méthode pour démarrer le niveau 1
        self.level = 1
        self.niveau_label.config(text="Niveau: 1")
        self.create_multiple_chocolates(5)

    def niveau2(self):
        # Méthode pour démarrer le niveau 2
        self.level = 2
        self.niveau_label.config(text="Niveau: 2")
        self.create_multiple_chocolates(10)

    def niveau3(self):
        # Méthode pour démarrer le niveau 3
        self.level = 3
        self.niveau_label.config(text="Niveau: 3")
        self.create_multiple_chocolates(15)

    def show_reward(self):
        # Méthode pour afficher la récompense en fonction du niveau atteint
        if self.level == 3:
            self.cookie_reward = 7500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau expert ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.level == 2:
            self.cookie_reward = 2500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau intermédiaire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.level == 1:
            self.cookie_reward = 750 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau débutant ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        else:
            self.cookie_reward = 250 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous pouvez mieux faire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        reward_label = tk.Label(self.master, text=reward, bg='#D3E6FF')
        reward_label.place(relx=0.5, rely=0.8, anchor="center")
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))

    def record(self):
        # Méthode pour enregistrer le record si le nombre de pépites est supérieur au record actuel
        if self.choco >= self.stat_instance.record_mn3:
            self.stat_instance.record_mn3 = self.cookie_reward
            self.stat_instance.label_record_mn3.config(text="Record du mini-jeu 3 : " + str(self.stat_instance.record_mn3) + " Cookies")

    def end_game(self):
        # Méthode pour terminer le jeu
        self.show_reward()
        self.record()
        self.game_started = False
        self.start_button.place_forget()
        self.timer_label.place_forget()
        self.clear_chocolates()  # Enlever pépites
