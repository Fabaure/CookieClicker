import tkinter as tk
from tkinter import PhotoImage
from math import *
from tkinter import font
class Upgrade:
    def __init__(self, master, cookie_instance, stat_instance, application_instance):
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.application_instance = application_instance
        self.auto_click = 0
        self.autoclick = False
        self.upgrade3 = False
        self.time_upgrade_3 = 300  # Temps 5min
        self.upgrade_price1 = 10
        self.upgrade_price2 = 20
        self.upgrade_price3 = 500
        self.avatar1 = 10000
        self.avatar2 = 50000
        self.avatar3 = 100000
        self.avatar4 = 500000
        self.niveau_upgrade1 = 0
        self.niveau_upgrade2 = 0
        self.niveau_upgrade3 = 0
        self.create_widgets()
        self.refreshcount_upgrade()
        self.check_avatar()

    def create_widgets(self):
        self.custom_font = font.Font(family="Cookies", size=10)
        self.imageB = tk.PhotoImage(file="BoutonUpgrade.png")

        self.upgrade_frame = tk.Frame(self.master, bg="white")
        self.upgrade_frame.place(relwidth=1, relheight=1)  # Expands frame to full window

        self.upgrade_button1 = tk.Button(self.upgrade_frame, image=self.imageB,
                                         text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies",
                                         anchor="center", command=self.buy_auto_click, borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")

        self.upgrade_button1.place(x=150, y=200)

        self.level_label1 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade1),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label1.place(x=450, y=240)

        self.upgrade_button2 = tk.Button(self.upgrade_frame, image=self.imageB, text=(
                                                                                         str(self.cookie_instance.cookie_multip + 1)) + " Cookies / Cliques\nPrix : " + str(
            self.upgrade_price2) + " Cookies", anchor="center", command=self.buy_clickdouble, borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")

        self.upgrade_button2.place(x=150, y=300)

        self.level_label2 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade2),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label2.place(x=450, y=340)

        self.upgrade_button3 = tk.Button(self.upgrade_frame, image=self.imageB,
                                         text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies",
                                         anchor="center", command=self.buy_5fois_cookie_all, borderwidth=0, bg="white",
                                         compound=tk.CENTER, activebackground="white", font=self.custom_font,
                                         fg="#612E18", activeforeground="#612E18", state="disabled")

        self.upgrade_button3.place(x=150, y=400)

        self.level_label3 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade3),
                                     font=self.custom_font, bg="white", fg="#612E18")
        self.level_label3.place(x=450, y=440)


        self.classy_button_image = PhotoImage(file="classy_cookie.png").subsample(2,2)
        self.formal_button_image = PhotoImage(file="formal_cookie.png").subsample(2,2)
        self.beach_button_image = PhotoImage(file="beach_cookie.png").subsample(2,2)
        self.funny_button_image = PhotoImage(file="funny_cookie.png").subsample(2,2)
        self.basic_button_image = PhotoImage(file="basic_cookie.png").subsample(2,2)


        self.avatar0_button = tk.Button(self.upgrade_frame, image=self.basic_button_image, bg="white",
                                        command=lambda: self.change_avatar(0), borderwidth=0, activebackground="white")
        self.avatar0_button.place(x=750, y=50)
        self.avatar1_button = tk.Button(self.upgrade_frame, image=self.classy_button_image, bg="white",
                                        command=lambda: self.change_avatar(1),
                                         state="disabled", borderwidth=0, activebackground="white")
        self.avatar1_button.place(x=600, y=200)
        self.avatar2_button = tk.Button(self.upgrade_frame, image=self.formal_button_image, bg="white",
                                        command=lambda: self.change_avatar(2),
                                         state="disabled", borderwidth=0, activebackground="white")
        self.avatar2_button.place(x=900, y=200)
        self.avatar3_button = tk.Button(self.upgrade_frame, image=self.beach_button_image, bg="white",
                                        command=lambda: self.change_avatar(3),
                                         state="disabled", borderwidth=0, activebackground="white")
        self.avatar3_button.place(x=600, y=350)
        self.avatar4_button = tk.Button(self.upgrade_frame, image=self.funny_button_image, bg="white",
                                        command=lambda: self.change_avatar(4),
                                         state="disabled", borderwidth=0, activebackground="white")
        self.avatar4_button.place(x=900, y=350)

        self.star = PhotoImage(file="magical_star.png").subsample(3,3)
        self.magical_button = tk.Button(self.upgrade_frame, image=self.star, bg='white', bd=0, relief=tk.SUNKEN,
                                       highlightthickness=0, command=self.activate_all, activebackground="white")
        self.magical_button.place(x=1020, y=80 )


    def update_levels(self):
        self.level_label1.config(text="Niveau: " + str(self.niveau_upgrade1))
        self.level_label2.config(text="Niveau: " + str(self.niveau_upgrade2))
        self.level_label3.config(text="Niveau: " + str(self.niveau_upgrade3))

    def refreshcount_upgrade(self):
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

        self.master.after(100, self.refreshcount_upgrade)
    def check_avatar(self):
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
        else :
            self.master.after(1000, self.check_avatar)
    def change_avatar(self, num_avatar):
        self.classy_image = PhotoImage(file="classy.png")
        self.formal_image = PhotoImage(file="formal.png")
        self.beach_image = PhotoImage(file="beach.png")
        self.funny_image = PhotoImage(file="funny.png")
        self.cookie_image = PhotoImage(file="cookie.png").zoom(2).subsample(4)

        if num_avatar == 0 :
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
        if self.cookie_instance.cookie_count >= self.upgrade_price1:
            self.niveau_upgrade1 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price1
            self.upgrade_price1 = ceil(self.upgrade_price1 * 1.8)
            self.upgrade_button1.config(text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies")
            self.auto_click += 1
            if not self.autoclick:
                self.autoclick = True
                self.fct_auto_click()
            self.update_levels()

    def fct_auto_click(self):
        self.cookie_instance.cookie_count += self.auto_click
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        self.master.after(1000, self.fct_auto_click)
        self.cookie_instance.refreshcount()


    def buy_clickdouble(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.niveau_upgrade2 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price2
            self.upgrade_price2 = ceil(self.upgrade_price2 * 2)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            self.cookie_instance.cookie_multip += 10
            self.upgrade_button2.config(text=(str(self.cookie_instance.cookie_multip+1))+" Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies")
        self.update_levels()


    def buy_5fois_cookie_all(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price3:
            self.niveau_upgrade3 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price2
            self.upgrade_price2 = ceil(self.upgrade_price2 * 2)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            print(self.cookie_instance.cookie_multip)
            print(self.auto_click)
            self.cookie_instance.cookie_multip *= 5 # Cliquer double * 5
            self.auto_click *= 5 # AutoClick * 5
            print(self.cookie_instance.cookie_multip)
            print(self.auto_click)
            if not self.upgrade3:
                self.upgrade3 = True
                self.upgrade_button3.config(state="disabled", text="All x5\nTemps restant: " + str(self.time_upgrade_3) + " secondes")
                self.fct_fois_cookie_all()
        self.update_levels()

    def fct_fois_cookie_all(self):
        self.time_upgrade_3 -= 1
        if self.time_upgrade_3 == 0:
            self.upgrade3 = False
            self.upgrade_button3.config(state="disabled", text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies")
        self.upgrade_button3.config(state="disabled",
                                    text="All x5\nTemps restant: " + str(self.time_upgrade_3) + " secondes")
        self.master.after(1000, self.fct_fois_cookie_all)

#fonction pour demo prof (à enlever après)
    def activate_all(self):
        self.avatar1_button.config(state="normal")
        self.avatar2_button.config(state="normal")
        self.avatar3_button.config(state="normal")
        self.avatar4_button.config(state="normal")

