import tkinter as tk

class Statistiques:
    def __init__(self, master):
        self.master = master
        self.stat_clique = 0
        self.stat_cookie = 0
        self.record_mn1 = 0
        self.record_mn2 = 0  # Initialize record for mini-jeu 2
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.master, text="Voici les statistiques !", font=("Courier", 15), fg="black", bg="white")
        self.label_title.pack(side="top", pady=20)

        self.stat_frame = tk.Frame(self.master, bg="white")
        self.stat_frame.pack(side="top")

        self.label_clique_nbr = tk.Label(self.stat_frame, text="Nombres de cliques : " + str(self.stat_clique), font=("Courier", 15), fg="black", bg="white")
        self.label_clique_nbr.pack(pady=2)

        self.label_cookie_nbr = tk.Label(self.stat_frame, text="Nombres de cookie total : " + str(self.stat_cookie), font=("Courier", 15), fg="black", bg="white")
        self.label_cookie_nbr.pack(pady=2)

        self.label_record_mn1 = tk.Label(self.stat_frame, text="Record du mini-jeu 1 : " + str(self.record_mn1) + " Cookie", font=("Courier", 15), fg="black", bg="white")
        self.label_record_mn1.pack(pady=2)

        self.label_record_mn2 = tk.Label(self.stat_frame, text="Record du mini-jeu 2 : " + str(self.record_mn2) + " Cookie", font=("Courier", 15), fg="black", bg="white")
        self.label_record_mn2.pack(pady=2)
