# Importation de modules
import tkinter as tk
from tkinter import PhotoImage  # Gestion d'images
from math import *
from tkinter import font  # Gestion de polices
import random
import time

class Upgrade:
    def __init__(self, master, cookie_instance, stat_instance, application_instance):
        # Initialisation de la classe Upgrade avec plusieurs instances et paramètres
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.application_instance = application_instance
        self.auto_click = 0  # Initialisation de l'auto-clic à 0
        self.autoclick = False
        self.upgrade3 = False
        self.time_upgrade_3 = 300# Temps 5min
        # Prix des différentes améliorations
        self.upgrade_price1 = 10
        self.upgrade_price2 = 20
        self.upgrade_price3 = 0
        self.upgrade_price4 = 0 #En cours
        # Prix des différents avatars
        self.avatar1 = 10000
        self.avatar2 = 50000
        self.avatar3 = 100000
        self.avatar4 = 500000
        # Niveaux des améliorations initialisé à 0
        self.level_upgrade1 = 0
        self.level_upgrade2 = 0
        self.level_upgrade3 = 0
        self.level_upgrade4 = 0
        self.indice_buyupgrade2 = 10
        self.is_spinning = False
        self.result = None
        self.create_widgets()  # Appel de la méthode pour créer les widgets
        self.refreshcount_upgrade()  # Appel de la méthode pour rafraîchir les états des boutons d'amélioration
        self.check_avatar()  # Appel de la méthode pour vérifier les avatars disponibles

    def create_widgets(self):
        self.custom_font = font.Font(family="Cookies", size=10)  # Définition d'une police personnalisée
        self.imageB = tk.PhotoImage(file="BoutonUpgrade.png")


        # Création d'un frame pour les améliorations
        self.upgrade_frame = tk.Frame(self.master, bg="white")
        self.upgrade_frame.place(relwidth=1, relheight=1)

        # Ajouter le titre "Boutique"
        self.title_label = tk.Label(self.upgrade_frame, text="Boutique", font=("Cookies", 60), bg='white', fg="#825D46")
        self.title_label.pack(pady=20)

        # Bouton pour la première amélioration (auto-clic)
        self.upgrade_button1 = tk.Button(self.upgrade_frame, image=self.imageB,
                                         text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies",
                                         anchor="center", command=self.buy_auto_click, borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button1.place(x=150, y=200)

        # Label pour afficher le niveau de la première amélioration
        self.level_label1 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.level_upgrade1),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label1.place(x=500, y=240)

        # Bouton pour la deuxième amélioration (augmentation du nombre de cookies par clic)
        self.upgrade_button2 = tk.Button(self.upgrade_frame, image=self.imageB, text="10 Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies", anchor="center", command=self.buy_clickplusdix, borderwidth=0, bg="white",compound=tk.CENTER, activebackground="white", font=self.custom_font,fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button2.place(x=150, y=300)

        # Label pour afficher le niveau de la deuxième amélioration
        self.level_label2 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.level_upgrade2),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label2.place(x=500, y=340)

        # Bouton pour la troisième amélioration ()
        self.upgrade_button3 = tk.Button(self.upgrade_frame, image=self.imageB,
                                         text="Roue de la fortune\nPrix : 1er tour gratuit !",
                                         anchor="center", command=self.spin, borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button3.place(x=150, y=400)

        # Label pour afficher le niveau de la troisième amélioration
        self.level_label3 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.level_upgrade3),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label3.place(x=500, y=440)

        self.upgrade_button4 = tk.Button(self.upgrade_frame, image=self.imageB,
                                         text="Upgrade 4\nProchainement",
                                         anchor="center", borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")

        self.upgrade_button4.place(x=150, y=500)

        self.level_label4 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.level_upgrade4),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label4.place(x=500, y=540)

        # Chargement et redimensionnement des images pour les boutons des avatars
        self.classy_button_image = PhotoImage(file="classy_cookie.png").subsample(2,2)
        self.formal_button_image = PhotoImage(file="formal_cookie.png").subsample(2,2)
        self.beach_button_image = PhotoImage(file="beach_cookie.png").subsample(2,2)
        self.funny_button_image = PhotoImage(file="funny_cookie.png").subsample(2,2)
        self.basic_button_image = PhotoImage(file="basic_cookie.png").subsample(2,2)

        # Boutons pour changer les avatars
        self.avatar0_button = tk.Button(self.upgrade_frame, image=self.basic_button_image, bg="white",
                                        command=lambda: self.change_avatar(0), borderwidth=0, activebackground="white")
        self.avatar0_button.place(x=840, y=120)

        self.avatar1_button = tk.Button(self.upgrade_frame, image=self.classy_button_image, bg="white",
                                        command=lambda: self.change_avatar(1),
                                        state="disabled", borderwidth=0, activebackground="white")
        self.avatar1_button.place(x=680, y=250)

        self.avatar_label1 = tk.Label(self.upgrade_frame, text="Se débloque à 10 000 cookies", bg="white", fg="#612E18")
        self.avatar_label1.place(x=690, y=390)

        self.avatar2_button = tk.Button(self.upgrade_frame, image=self.formal_button_image, bg="white",
                                        command=lambda: self.change_avatar(2),
                                        state="disabled", borderwidth=0, activebackground="white")
        self.avatar2_button.place(x=1000, y=250)

        self.avatar_label2 = tk.Label(self.upgrade_frame, text="Se débloque à 50 000 cookies", bg="white", fg="#612E18")
        self.avatar_label2.place(x=1010, y=390)

        self.avatar3_button = tk.Button(self.upgrade_frame, image=self.beach_button_image, bg="white",
                                        command=lambda: self.change_avatar(3),
                                        state="disabled", borderwidth=0, activebackground="white")
        self.avatar3_button.place(x=680, y=420)

        self.avatar_label3 = tk.Label(self.upgrade_frame, text="Se débloque à 100 000 cookies", bg="white", fg="#612E18")
        self.avatar_label3.place(x=690, y=560)

        self.avatar4_button = tk.Button(self.upgrade_frame, image=self.funny_button_image, bg="white",
                                        command=lambda: self.change_avatar(4),
                                        state="disabled", borderwidth=0, activebackground="white")
        self.avatar4_button.place(x=1000, y=420)

        self.avatar_label4 = tk.Label(self.upgrade_frame, text="Se débloque à 500 000 cookies", bg="white", fg="#612E18")
        self.avatar_label4.place(x=1010, y=560)

        # Bouton magique pour activer tous les boutons (pour la démonstration)
        self.star = PhotoImage(file="magical_star.png").subsample(3,3)
        self.magical_button = tk.Button(self.upgrade_frame, image=self.star, bg='white', bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.activate_all, activebackground="white")
        self.magical_button.place(x=1060, y=50)

    def update_levels(self):
        # Mise à jour des niveaux des améliorations dans les labels
        self.level_label1.config(text="Niveau: " + str(self.level_upgrade1))
        self.level_label2.config(text="Niveau: " + str(self.level_upgrade2))
        self.level_label3.config(text="Niveau: " + str(self.level_upgrade3))

    def refreshcount_upgrade(self):
        # Activation ou désactivation des boutons d'amélioration en fonction du nombre de cookies
        if self.cookie_instance.cookie_count >= self.upgrade_price1:
            self.upgrade_button1.config(state="normal")
        else:
            self.upgrade_button1.config(state="disabled")

        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.upgrade_button2.config(state="normal")
        else:
            self.upgrade_button2.config(state="disabled")

        if self.cookie_instance.cookie_count >= self.upgrade_price3 and self.upgrade3 == False:
            self.upgrade_button3.config(state="normal")
        else:
            self.upgrade_button3.config(state="disabled")

        # Rappel de la méthode toutes les 100 ms pour vérifier l'état des améliorations
        self.master.after(100, self.refreshcount_upgrade)

    def check_avatar(self):
        # Vérification et activation des avatars en fonction du nombre de cookies
        if self.cookie_instance.cookie_count >= self.avatar1 and self.avatar1 != 0:
            self.avatar1 = 0
            self.avatar1_button.config(state = "normal")
            self.master.after(1000, self.check_avatar)
        elif self.cookie_instance.cookie_count >= self.avatar2 and self.avatar2 != 0:
            self.avatar2 = 0
            self.avatar2_button.config(state = "normal")
            self.master.after(1000, self.check_avatar)
        elif self.cookie_instance.cookie_count >= self.avatar3 and self.avatar3 != 0:
            message = "\n\n Vous avez débloqué l'avatar 3!\n\nRendez-vous dans la page Boutique pour pouvoir le tester!"
            self.application_instance.display_message(message)
            self.avatar3 = 0
            self.avatar3_button.config(state = "normal")
        elif self.cookie_instance.cookie_count >= self.avatar4 and self.avatar4 != 0:
            message = "\n\n Vous avez débloqué l'avatar 4!\n\nRendez-vous dans la page Boutique pour pouvoir le tester!"
            self.application_instance.display_message(message)
            self.avatar4 = 0
            self.avatar4_button.config(state = "normal")
        else:
            self.master.after(1000, self.check_avatar)  # Rappel de la méthode toutes les secondes

    def change_avatar(self, num_avatar):

        # Initialisation des images d'avatars et redimensionnement
        self.classy_image = PhotoImage(file="classy.png")
        self.formal_image = PhotoImage(file="formal.png")
        self.beach_image = PhotoImage(file="beach.png")
        self.funny_image = PhotoImage(file="funny.png")
        self.cookie_image = PhotoImage(file="cookie.png").zoom(2).subsample(4)

        # Changement de l'image de l'avatar en fonction du numéro choisi
        if num_avatar == 0:
            self.cookie_instance.cookie_button.config(image=self.cookie_image)
        elif num_avatar == 1:
            self.cookie_instance.cookie_button.config(image=self.classy_image)
        elif num_avatar == 2:
            self.cookie_instance.cookie_button.config(image=self.formal_image)
        elif num_avatar == 3:
            self.cookie_instance.cookie_button.config(image=self.beach_image)
        else:
            self.cookie_instance.cookie_button.config(image=self.funny_image)

    def buy_auto_click(self):
        # Achat de l'amélioration auto-clic
        if self.cookie_instance.cookie_count >= self.upgrade_price1:
            self.level_upgrade1 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price1
            self.upgrade_price1 = ceil(self.upgrade_price1 * 1.5)
            self.upgrade_button1.config(text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies")
            self.auto_click += 1
            if not self.autoclick:
                self.autoclick = True
                self.fct_auto_click()
            self.update_levels()

    def fct_auto_click(self):
        # Fonction de l'auto-clic
        self.cookie_instance.cookie_count += self.auto_click
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        self.master.after(1000, self.fct_auto_click)
        self.cookie_instance.refreshcount()

    def buy_clickplusdix(self):
        # Achat de l'amélioration du click +10
        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.level_upgrade2 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price2
            self.upgrade_price2 = ceil(self.upgrade_price2 * 2.5)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            if self.cookie_instance.cookie_multip == 1:
                self.cookie_instance.cookie_multip += 9
            else:
                self.cookie_instance.cookie_multip += 10
            self.indice_buyupgrade2 += 10
            self.upgrade_button2.config(text=str(self.indice_buyupgrade2) + " Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies")
        self.update_levels()

    def spin(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price3:
            self.level_upgrade3 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price3
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            self.upgrade_button3.config(text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies", state="disabled")

            self.spin_root = tk.Toplevel()
            self.frame = tk.Frame(self.spin_root)
            self.frame.pack()

            self.choice_label = tk.Label(self.frame, text="", font=("Helvetica", 20))
            self.choice_label.pack()

            self.choices_list = ["50 000 Cookies", "10 000 Cookies", "5 000 Cookies", "1 000 Cookies", "500 Cookies", "100 Cookies", "10 Cookies"]
            self.is_spinning = True
            self.upgrade_price3 = 15000
            self.upgrade_button3.config(text="Roue de la fortune\nPrix : " + str(self.upgrade_price3) + " Cookies",
                                        state="normal")

            self.animate(self.choices_list)
        self.update_levels()



    def animate(self, choices_list):
        for i in range(20):
            choice = random.choice(choices_list)
            self.choice_label.config(text=choice)
            self.spin_root.update()
            time.sleep(0.1)  # Délai entre chaque changement de choix

        self.result = random.choice(choices_list)
        self.choice_label.config(text=self.result, fg="red")
        self.is_spinning = False
        self.spin_root.after(3000, self.spin_root.destroy)

        if self.result == "50 000 Cookies":
            self.cookie_instance.cookie_count += 50000
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        elif self.result == "10 000 Cookies":
            self.cookie_instance.cookie_count += 10000
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        elif self.result == "5 000 Cookies":
            self.cookie_instance.cookie_count += 5000
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        elif self.result == "1 000 Cookies":
            self.cookie_instance.cookie_count += 1000
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        elif self.result == "500 Cookies":
            self.cookie_instance.cookie_count += 500
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        elif self.result == "100 Cookies":
            self.cookie_instance.cookie_count += 100
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        else:
            self.cookie_instance.cookie_count += 10
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))

    def activate_all(self):
        # Fonction pour démonstration (à enlever après) qui active tous les boutons avatars
        self.avatar1_button.config(state="normal")
        self.avatar2_button.config(state="normal")
        self.avatar3_button.config(state="normal")
        self.avatar4_button.config(state="normal")
