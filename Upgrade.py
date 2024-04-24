from Cookie import Cookie
import tkinter as tk
from math import *
class Upgrade:
    def __init__(self, master, cookie_instance):
        self.master = master
        self.cookie_instance = cookie_instance
        self.auto_click = 0
        self.autoclick = False
        self.upgrade_price1 = 10
        self.upgrade_price2 = 20
        self.upgrade_price3 = 500
        self.create_widgets()

    def create_widgets(self):
        self.upgrade_frame = tk.Frame(self.master, bg="white")
        self.upgrade_frame.pack(expand=True, side="bottom", padx=10, pady=10)

        self.upgrade_button1 = tk.Button(self.upgrade_frame, text="Auto-click\nPrix : " + str(self.upgrade_price1) + " Cookies", anchor="center", command=self.buy_auto_click, height=3,width=50, bg='#E2BFB3')
        self.upgrade_button1.pack(pady=10)

        self.upgrade_button2 = tk.Button(self.upgrade_frame, text=(str(self.cookie_instance.cookie_multip+1)) +" Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies", anchor="center", command=self.buy_clickdouble, height=3, width=50, bg='#E2BFB3')
        self.upgrade_button2.pack(pady=10)

        self.upgrade_button3 = tk.Button(self.upgrade_frame, text="Upgrade 3\nPrix : " + str(self.upgrade_price3) + " Cookies", anchor="center", command=self.buy_upgrade3, height=3, width=50, bg='#E2BFB3', state="disabled")
        self.upgrade_button3.pack(pady=10)

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

    def buy_clickdouble(self):
        if self.cookie_instance.cookie_count >= self.upgrade_price2:
            self.cookie_instance.cookie_count -= self.upgrade_price2
            self.upgrade_price2 = ceil(self.upgrade_price2 * 1.5)
            self.cookie_instance.label_cookie_count.config(text="Cookies : " + str(self.cookie_instance.cookie_count))
            self.cookie_instance.cookie_multip += 1
            self.upgrade_button2.config(text=(str(self.cookie_instance.cookie_multip+1))+" Cookies / Cliques\nPrix : " + str(self.upgrade_price2) + " Cookies")

    def buy_upgrade3(self):
        None