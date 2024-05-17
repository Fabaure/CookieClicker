import tkinter as tk
from tkinter import PhotoImage
from math import *
class Minijeu2:

    def __init__(self, master, stat_instance, cookie_instance):
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.master.title("Sauve ton cookie!")
        self.master.geometry("600x600")

        self.cookie_reward = 0
        self.level = 0
        self.game_started = False
        self.monstre_niveau1_clicks = 0
        self.monstre_niveau2_clicks = 0
        self.monstre_niveau3_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        side_frame = tk.Frame(self.master)
        side_frame.pack(side="top", padx=10)

        rules_text = ("Bonjour et bienvenue à notre deuxième mini-jeu !"
                      "\n Dans celui-ci, la rapidité est la clé, alors soyez vif. "
                      "\n Défendez votre cookie de macaron le glouton en cliquant sur lui lorsqu'il apparait. "
                      "\n Appuyez plusieurs fois jusqu'à ca qu'il disparaisse "
                      "\n Attention il est de plus en plus énervé, franchi les 3 niveaux"
                      "\n Si vous n'arriver pas à battre macaron le glouton à temps vous avez perdu"
                      "\n Tentez de décrocher les meilleures récompenses ! "
                      "\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center")
        rules_label.pack(side="top", pady=20)

        self.niveau_label = tk.Label(self.master, text="Niveau: 0")
        self.niveau_label.pack(pady=10)

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="")
        self.timer_label.pack(pady=10)

        self.cookie_image = PhotoImage(file="cookie.png").subsample(3, 3)
        self.cookie_label = tk.Label(self.master, image=self.cookie_image, borderwidth=0)
        self.cookie_label.pack(pady=20, side="left", padx=30)

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.cookies = 0
            self.niveau_label.config(text="Niveau: 1")
            self.start_button.pack_forget()
            self.timer_label.pack()
            self.countdown(60)
            self.monstre_niveau1()

    def countdown(self, count):
        if count >= 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            if self.game_started == True:
                self.end_game()

    def monstre_niveau1(self):
        # Créer le bouton du monstre niveau 1
        self.monstre_image = PhotoImage(file="monstrecontent.png").subsample(4, 4)
        self.monstre_button = tk.Button(self.master, image=self.monstre_image, command=self.monstre_action, borderwidth=0)
        self.monstre_button.pack(pady=20, side="right", padx=30)

    def monstre_action(self):
        self.monstre_niveau1_clicks += 1  # Incrémenter le compteur de clics du monstre
        if self.monstre_niveau1_clicks == 100:
            self.level += 1
            self.monstre_button.pack_forget()  # Faire disparaître le bouton du monstre une fois que le compteur atteint 10
            self.monstre_niveau2()

    def monstre_niveau2(self):
        # Créer le bouton du monstre niveau 2
        self.monstre_niveau2_image = PhotoImage(file="monstredecu.png").subsample(2, 2)
        self.monstre_niveau2_button = tk.Button(self.master, image=self.monstre_niveau2_image, command=self.monstre_niveau2_action, borderwidth=0)
        self.monstre_niveau2_button.pack(pady=20, side="right")

    def monstre_niveau2_action(self):
        self.niveau_label.config(text="Niveau: 2")
        self.monstre_niveau2_clicks += 1
        # Incrémenter le compteur de clics du monstre niveau 2
        if self.monstre_niveau2_clicks == 150:
            self.level += 1
            self.monstre_niveau2_button.pack_forget()  # Faire disparaître le bouton du monstre niveau 2 une fois que le compteur atteint 10
            self.monstre_niveau3()

    def monstre_niveau3(self):
        # Créer le bouton du monstre niveau 3
        self.monstre_niveau3_image = PhotoImage(file="monstreenerve.png").subsample(2, 2)
        self.monstre_niveau3_button = tk.Button(self.master, image=self.monstre_niveau3_image, command=self.monstre_niveau3_action, borderwidth=0)
        self.monstre_niveau3_button.pack(pady=20)

    def monstre_niveau3_action(self):
        self.niveau_label.config(text="Niveau: 3")
        self.monstre_niveau3_clicks += 1
        if self.monstre_niveau3_clicks == 200 :
            self.level += 1
            self.end_game()
    def show_reward(self):
        if self.level == 3:
            self.monstre_niveau3_button.pack_forget()  # Faire disparaître le bouton du monstre niveau 3 une fois que le compteur atteint 10
            self.center_cookie()
            self.cookie_reward = 7500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau expert ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.level == 2:
            self.monstre_niveau3_button.pack_forget()
            self.cookie_reward = 2500 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau intermédiaire ! Vous avez gagné " + str(self.cookie_reward) + "Cookies"
            self.monstre_perdu()
        elif self.level == 1:
            self.monstre_niveau2_button.pack_forget()
            self.cookie_reward = 750 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous avez débloqué le niveau débutant ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
            self.monstre_perdu()
        else:
            self.monstre_button.pack_forget()
            self.cookie_reward = 250 + ceil(self.level * 250)
            self.cookie_instance.cookie_count += self.cookie_reward
            self.cookie_instance.refreshcount()
            reward = "Vous pouvez mieux faire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
            self.monstre_perdu()
        reward_label = tk.Label(self.master, text=reward)
        reward_label.pack(pady=10)
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))

    def record(self):
        if self.cookies >= self.stat_instance.record_mn2:
            self.stat_instance.record_mn2 = self.cookie_reward
            self.stat_instance.label_record_mn2.config(text="Record du mini-jeu 2 : " + str(self.stat_instance.record_mn2) + " Cookies")

    def monstre_perdu(self):
        # Afficher le monstre avec le cookie lors de la fin du jeu
        self.cookie_label.pack_forget()
        self.monstre_perdu_image = PhotoImage(file="monstreaveccookie.png").subsample(2, 2)
        self.monstre_perdu_label = tk.Label(self.master, image=self.monstre_perdu_image, borderwidth=0)
        self.monstre_perdu_label.pack(pady=20, padx=30)

    def center_cookie(self):
        # Remove the cookie label from its current position
        self.cookie_label.pack_forget()

        # Repack the cookie label in the middle of the window
        self.cookie_label.pack(pady=20)

    def end_game(self):

        self.show_reward()
        self.record()
        self.game_started = False
        self.start_button.pack_forget()
        self.timer_label.pack_forget()

