# Importation de modules
import tkinter as tk
from tkinter import messagebox, Listbox  # Boîtes de dialogue et Listbox

class Statistiques:
    def __init__(self, master, app_instance):
        # Initialisation de la classe Statistiques
        self.master = master
        self.app_instance = app_instance
        # Initialisation des compteurs à 0
        self.stat_clique = 0
        self.stat_cookie = 0
        self.record_mn1 = 0
        self.record_mn2 = 0
        self.record_mn3 = 0

        self.scores = []  # Liste pour stocker les scores des joueurs
        self.load_scores()  # Charger les scores depuis un fichier

        self.create_widgets()  # Créer les widgets de l'interface graphique

    def create_widgets(self):
        # Création et configuration des widgets pour l'interface graphique
        self.stat_frame = tk.Frame(self.master, bg=self.app_instance.bg_main)
        self.stat_frame.pack(expand=True)

        # Affichage du temps de jeu
        self.time_label = tk.Label(self.stat_frame, text=f"Temps de jeu: 00:00:00", font=("Courier", 15), fg=self.app_instance.font,
                                    bg=self.app_instance.bg_main)
        self.time_label.pack(side="top", pady=20)

        # Titre des statistiques
        self.label_title = tk.Label(self.stat_frame, text="Voici les statistiques !", font=("Courier", 15), fg=self.app_instance.font,
                                    bg=self.app_instance.bg_main)
        self.label_title.pack(side="top", pady=20)

        # Affichage du nombre de clics
        self.label_clique_nbr = tk.Label(self.stat_frame, text="Nombres de cliques : " + str(self.stat_clique),
                                         font=("Courier", 15), fg=self.app_instance.font, bg=self.app_instance.bg_main)
        self.label_clique_nbr.pack(pady=2)

        # Affichage du record de cookies
        self.label_cookie_nbr = tk.Label(self.stat_frame, text="Record du nombres de cookie : " + str(self.stat_cookie),
                                         font=("Courier", 15), fg=self.app_instance.font, bg=self.app_instance.bg_main)
        self.label_cookie_nbr.pack(pady=2)

        # Affichage des records des mini-jeux
        self.label_record_mn1 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 1 : " + str(self.record_mn1) + " Cookie",
                                         font=("Courier", 15), fg=self.app_instance.font, bg=self.app_instance.bg_main)
        self.label_record_mn1.pack(pady=2)

        self.label_record_mn2 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 2 : " + str(self.record_mn2) + " Cookie",
                                         font=("Courier", 15), fg=self.app_instance.font, bg=self.app_instance.bg_main)
        self.label_record_mn2.pack(pady=2)

        self.label_record_mn3 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 3 : " + str(self.record_mn3) + " Cookie",
                                         font=("Courier", 15), fg=self.app_instance.font, bg=self.app_instance.bg_main)
        self.label_record_mn3.pack(pady=2)

        # Cadre pour le classement général
        self.rank_frame = tk.Frame(self.master, bg=self.app_instance.bg_main)
        self.rank_frame.pack(expand=True, side="bottom")

        # Titre du classement général
        self.label_rank = tk.Label(self.rank_frame, text="Voici le classement général du Cookie Clicker !", font=("Courier", 15), fg=self.app_instance.font,bg=self.app_instance.bg_main)
        self.label_rank.pack(pady=10)

        # Listbox pour afficher les scores des joueurs
        self.listbox_scores = tk.Listbox(self.rank_frame, width=50, height=20)
        self.listbox_scores.pack()

        # Mise à jour de l'affichage des scores
        self.update_scores_display()

    def save_score(self):
        # Sauvegarde du score actuel du joueur
        name = self.app_instance.player_name
        self.score = self.stat_cookie
        self.scores.append((name, self.score))
        self.scores.sort(key=lambda x: x[1], reverse=True)  # Trier les scores par ordre décroissant
        self.save_scores_to_file()
        if hasattr(self, 'listbox_scores') and self.listbox_scores.winfo_exists():
            self.update_scores_display()
        self.master.quit()

    def load_scores(self):
        # Charger les scores depuis un fichier
        try:
            with open("scores.txt", "r") as file:
                for line in file:
                    name, score = line.strip().split(": ")
                    self.scores.append((name, int(score)))
            self.scores.sort(key=lambda x: x[1], reverse=True)
        except FileNotFoundError:
            pass

    def save_scores_to_file(self):
        # Enregistrer les scores dans un fichier
        with open("scores.txt", "w") as file:
            for name, score in self.scores:
                file.write(f"{name}: {score}\n")

    def update_scores_display(self):
        # Mettre à jour l'affichage des scores dans la Listbox
        if hasattr(self, 'listbox_scores'):
            self.listbox_scores.delete(0, tk.END)
            for name, score in self.scores:
                self.listbox_scores.insert(tk.END, f"{name}: {score}")  # Ajouter chaque score à la Listbox
