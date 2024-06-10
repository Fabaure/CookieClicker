import tkinter as tk
from tkinter import PhotoImage
from math import *
class Upgrade:
    def __init__(self, master, cookie_instance, stat_instance):
        self.master = master
        self.stat_instance = stat_instance
        self.cookie_instance = cookie_instance
        self.auto_click = 0
        self.autoclick = False
        self.upgrade_price1 = 10
        self.upgrade_price2 = 20
        self.upgrade_price3 = 500
        self.create_widgets()

    def create_widgets(self):
        self.upgrade_frame = tk.Frame(self.master, bg="white")
        self.upgrade_frame.place(relwidth=1, relheight=1)  # Expands frame to full window

        self.upgrade_button1 = tk.Button(self.upgrade_frame,
                                         text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies",
                                         anchor="center", command=self.buy_auto_click, height=3, width=50, bg='#E2BFB3')
        self.upgrade_button1.place(x=250, y=200)

        self.upgrade_button2 = tk.Button(self.upgrade_frame, text=(
                                                                      str(self.cookie_instance.cookie_multip + 1)) + " Cookies / Clique\nPrix : " + str(
            self.upgrade_price2) + " Cookies", anchor="center", command=self.buy_clickdouble, height=3, width=50,
                                         bg='#E2BFB3')
        self.upgrade_button2.place(x=250, y=270)

        self.upgrade_button3 = tk.Button(self.upgrade_frame,
                                         text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies",
                                         anchor="center", command=self.buy_upgrade3, height=3, width=50, bg='#E2BFB3',
                                         state="disabled")
        self.upgrade_button3.place(x=250, y=340)



        self.classy_button_image = PhotoImage(file="classy_cookie.png").subsample(2,2)
        self.formal_button_image = PhotoImage(file="formal_cookie.png").subsample(2,2)
        self.beach_button_image = PhotoImage(file="beach_cookie.png").subsample(2,2)
        self.funny_button_image = PhotoImage(file="funny_cookie.png").subsample(2,2)
        self.basic_button_image = PhotoImage(file="basic_cookie.png").subsample(2,2)


        self.avatar0_button = tk.Button(self.upgrade_frame, image=self.basic_button_image, bg="white",
                                        command=lambda: self.change_avatar(0), borderwidth=0)
        self.avatar0_button.place(x=750, y=50)
        self.avatar1_button = tk.Button(self.upgrade_frame, image=self.classy_button_image, bg="white",
                                        command=lambda: self.change_avatar(1),
                                         state="disabled", borderwidth=0)
        self.avatar1_button.place(x=600, y=200)
        self.avatar2_button = tk.Button(self.upgrade_frame, image=self.formal_button_image, bg="white",
                                        command=lambda: self.change_avatar(2),
                                         state="disabled", borderwidth=0)
        self.avatar2_button.place(x=900, y=200)
        self.avatar3_button = tk.Button(self.upgrade_frame, image=self.beach_button_image, bg="white",
                                        command=lambda: self.change_avatar(3),
                                         state="disabled", borderwidth=0)
        self.avatar3_button.place(x=600, y=350)
        self.avatar4_button = tk.Button(self.upgrade_frame, image=self.funny_button_image, bg="white",
                                        command=lambda: self.change_avatar(4),
                                         state="disabled", borderwidth=0)
        self.avatar4_button.place(x=900, y=350)

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
            self.cookie_instance.cookie_count -= self.upgrade_price1
            self.upgrade_price1 = ceil(self.upgrade_price1 * 1.8)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            self.upgrade_button1.config(text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies")
            self.auto_click += 1
            if not self.autoclick:
                self.autoclick = True
                self.fct_auto_click()

    def fct_auto_click(self):
        self.cookie_instance.cookie_count += self.auto_click
        self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
        self.master.after(1000, self.fct_auto_click)
        self.cookie_instance.refreshcount()
    def buy_clickdouble(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.cookie_instance.cookie_count -= self.upgrade_price2
            self.upgrade_price2 = ceil(self.upgrade_price2 * 1.5)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            self.cookie_instance.cookie_multip += 1
            self.upgrade_button2.config(text=(str(self.cookie_instance.cookie_multip+1))+" Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies")

    def buy_upgrade3(self):
        None