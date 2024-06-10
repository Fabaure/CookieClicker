from Cookie import Cookie
import tkinter as tk
from math import *
from tkinter import PhotoImage
from tkinter import font

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
        self.niveau_upgrade1 = 0
        self.niveau_upgrade2 = 0
        self.niveau_upgrade3 = 0
        self.imageB = tk.PhotoImage(file="BoutonUpgrade.png")
        self.custom_font = font.Font(family="Cookies", size=10)
        self.create_widgets()
        self.refreshcount_upgrade()

    def create_widgets(self):
        self.upgrade_frame = tk.Frame(self.master, bg="white")
        self.upgrade_frame.pack(side="left", expand=True, padx=10, pady=10)

        self.upgrade_button1 = tk.Button(self.upgrade_frame, image=self.imageB,text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies",anchor="center", command=self.buy_auto_click, borderwidth=0, bg="white",compound=tk.CENTER, activebackground="white", font=self.custom_font,fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button1.grid(row=0, column=0, pady=10)

        self.level_label1 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade1), font=self.custom_font, bg="white",fg="#612E18")
        self.level_label1.grid(row=0, column=1, pady=10)

        self.upgrade_button2 = tk.Button(self.upgrade_frame, image=self.imageB, text=(str(self.cookie_instance.cookie_multip + 1)) + " Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies", anchor="center", command=self.buy_clickdouble, borderwidth=0, bg="white",compound=tk.CENTER, activebackground="white", font=self.custom_font,fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button2.grid(row=1, column=0, pady=10)

        self.level_label2 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade2), font=self.custom_font, bg="white",fg="#612E18")
        self.level_label2.grid(row=1, column=1, pady=10)

        self.upgrade_button3 = tk.Button(self.upgrade_frame, image=self.imageB,text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies",anchor="center", command=self.buy_upgrade3, borderwidth=0, bg="white",compound=tk.CENTER, activebackground="white", font=self.custom_font,fg="#612E18", activeforeground="#612E18", state="disabled")
        self.upgrade_button3.grid(row=2, column=0, pady=10)

        self.level_label3 = tk.Label(self.upgrade_frame, text="Niveau: " + str(self.niveau_upgrade3), font=self.custom_font, bg="white",fg="#612E18")
        self.level_label3.grid(row=2, column=1, pady=10)

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

        if self.cookie_instance.cookie_count >= self.upgrade_price3:
            self.upgrade_button3.config(state="normal")
        else:
            self.upgrade_button3.config(state="disabled")

        self.master.after(100, self.refreshcount_upgrade)

    def buy_auto_click(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price1:
            self.niveau_upgrade1 += 1
            self.cookie_instance.cookie_count -= self.upgrade_price1
            self.upgrade_price1 = ceil(self.upgrade_price1 * 1.8)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
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

    def buy_upgrade3(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.niveau_upgrade3 += 1
        self.update_levels()