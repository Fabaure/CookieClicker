import tkinter as tk
from tkinter import PhotoImage
from math import *


class Minijeu1:

    def __init__(self, master, cookie_instance, stat_instance):
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.master.title("Cookie Clicker")
        self.master.geometry("600x600")
        self.cookies = 0
        self.game_started = False
        self.cookie_reward = 0

        self.create_widgets()

    def create_widgets(self):

        side_frame = tk.Frame(self.master)
        side_frame.pack(side="top", padx=10)

        rules_text = ( "Bonjour et bienvenue à notre premier mini-jeu !\n Dans celui-ci, la rapidité est la clé, alors soyez vif et ne vous trompez pas. "
"\n Vous disposez de trente secondes pour cliquer autant de fois que possible sur le cookie. "
"\n Dépêchez-vous et tentez de décrocher les meilleures récompenses ! "
"\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify= "center")
        rules_label.pack(side="top", pady=20)

        self.cookies_label = tk.Label(self.master, text="Cookies: 0")
        self.cookies_label.pack(pady=10)

        self.label_record_mn1 = tk.Label(self.master, text=str(self.stat_instance.record_mn1) + " Cookie")
        self.label_record_mn1.pack(pady=5)

        self.cookie_image = PhotoImage(file="cookie.png").subsample(3, 3)
        self.cookie_button = tk.Button(self.master, image=self.cookie_image, command=self.click_cookie, state="disabled", borderwidth=0)
        self.cookie_button.pack(pady=30)

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="")

    def click_cookie(self):
        if self.game_started:
            self.cookies += 1
            self.cookies_label.config(text="Cookies: " + str(self.cookies))

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.cookies = 0
            self.cookies_label.config(text="Cookies: 0")
            self.start_button.pack_forget()
            self.timer_label.pack()
            self.cookie_button.config(state="normal")
            self.countdown(3)

    def countdown(self, count):
        if count > 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.show_reward()
            self.record()
            self.end_game()

    def show_reward(self):
        if self.cookies >= 300:
            self.cookie_reward = 5000 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            reward = "Vous avez débloqué le niveau expert ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.cookies >= 200:
            self.cookie_reward = 1000 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            reward = "Vous avez débloqué le niveau intermédiaire ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        elif self.cookies >= 100:
            self.cookie_reward = 500 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            reward = "Vous avez débloqué le niveau débutant ! Vous avez gagné " + str(self.cookie_reward) + " Cookies"
        else:
            self.cookie_reward = 100 + ceil(self.cookies * 2.5)
            self.cookie_instance.cookie_count += self.cookie_reward
            reward = "Vous pouvez mieux faire ! Vous avez gagné " + str(self.cookie_reward) +" Cookies"
        reward_label = tk.Label(self.master, text=reward)
        reward_label.pack(pady=10)
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))

    def record(self):
        if self.cookies >= self.stat_instance.record_mn1:
            self.stat_instance.record_mn1 = self.cookies
            self.label_record_mn1.config(text="Record : " + str(self.cookies) + " Cookies")
            self.stat_instance.label_record_mn1.config(text="Record du mini-jeu 1 : " + str(self.stat_instance.record_mn1) + " Cookies")

    def end_game(self):
        self.game_started = False
        self.cookie_button.config(state="disabled")
        self.start_button.pack_forget()
        self.timer_label.pack_forget()

