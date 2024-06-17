# Importation de modules
import tkinter as tk
from tkinter import PhotoImage  # Gestion d'images


class Cookie:
    def __init__(self, master, stat_instance, application_instance):
        self.master = master
        self.stat_instance = stat_instance  # Instance de statistiques pour suivre les statistiques du jeu
        self.application_instance = application_instance  # Instance de l'application principale

        # Chargement et configuration de l'image du cookie
        self.image = PhotoImage(file="Assets/Images/cookie.png").zoom(2).subsample(4)

        # Initialisation des variables de jeu
        self.cookie_count = 0
        self.cookie_multip = 1
        self.clique = 0

        # Création des widgets de l'interface graphique
        self.create_widgets()

    def create_widgets(self):
        # Création d'un cadre pour les différents éléments
        self.cookie_frame = tk.Frame(self.master, bg=self.application_instance.bg_main)
        self.cookie_frame.pack(expand=True)

        # Label pour afficher le nombre de cookies collectés
        self.label_cookie_count = tk.Label(self.cookie_frame, text="Cookie : " + str(self.cookie_count),
                                           font=("Courier", 15), fg="black", bg=self.application_instance.bg_main)
        self.label_cookie_count.pack(side="top", pady=20)

        # Bouton cookie
        self.cookie_button = tk.Button(self.cookie_frame, image=self.image, bg=self.application_instance.bg_main, bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.add_cookie, activebackground="white")
        self.cookie_button.pack()

    def add_cookie(self):
        # Méthode lors d'un clic de cookie
        self.stat_instance.stat_clique += 1
        self.cookie_count += self.cookie_multip
        self.label_cookie_count.config(text="Cookies : " + str(self.cookie_count))

        # Mise à jour de l'affichage du nombre de clics dans les statistiques
        self.stat_instance.label_clique_nbr.config(text="Nombres de cliques : " + str(self.stat_instance.stat_clique))

        # Vérification si le nombre de cookies dépasse le record actuel dans les statistiques
        if self.cookie_count >= self.stat_instance.stat_cookie:
            self.refreshcount()

    def refreshcount(self):
        # Met à jour le record du nombre de cookies dans les statistiques
        if self.cookie_count >= self.stat_instance.stat_cookie:
            self.stat_instance.stat_cookie = self.cookie_count
            self.master.after(1, self.stat_instance.label_cookie_nbr.config(
                text="Record du nombres de cookie :" + str(self.cookie_count)))