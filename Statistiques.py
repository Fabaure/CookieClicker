import tkinter as tk
from tkinter import messagebox, Listbox

class Statistiques:
    def __init__(self, master, app_instance):
        self.master = master
        self.app_instance = app_instance
        self.stat_clique = 0
        self.stat_cookie = 0
        self.record_mn1 = 0
        self.record_mn2 = 0
        self.record_mn3 = 0

        self.scores = []
        self.load_scores()


        self.create_widgets()

    def create_widgets(self):
        self.stat_frame = tk.Frame(self.master, bg="white")
        self.stat_frame.pack(expand=True, side="top")

        self.time_label = tk.Label(self.stat_frame, text=f"Temps de jeu: 00:00:00", font=("Courier", 15), fg="black",
                                    bg="white")
        self.time_label.pack(side="top", pady=20)

        self.label_title = tk.Label(self.stat_frame, text="Voici les statistiques !", font=("Courier", 15), fg="black",
                                    bg="white")
        self.label_title.pack(side="top", pady=20)

        self.label_clique_nbr = tk.Label(self.stat_frame, text="Nombres de cliques : " + str(self.stat_clique),
                                         font=("Courier", 15), fg="black", bg="white")
        self.label_clique_nbr.pack(pady=2)

        self.label_cookie_nbr = tk.Label(self.stat_frame, text="Record du nombres de cookie : " + str(self.stat_cookie),
                                         font=("Courier", 15), fg="black", bg="white")
        self.label_cookie_nbr.pack(pady=2)

        self.label_record_mn1 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 1 : " + str(self.record_mn1) + " Cookie",
                                         font=("Courier", 15), fg="black", bg="white")
        self.label_record_mn1.pack(pady=2)

        self.label_record_mn2 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 2 : " + str(self.record_mn2) + " Cookie",
                                         font=("Courier", 15), fg="black", bg="white")
        self.label_record_mn2.pack(pady=2)

        self.label_record_mn3 = tk.Label(self.stat_frame,
                                         text="Record du mini-jeu 3 : " + str(self.record_mn3) + " Cookie",
                                         font=("Courier", 15), fg="black", bg="white")
        self.label_record_mn3.pack(pady=2)

        self.rank_frame = tk.Frame(self.master, bg="white")
        self.rank_frame.pack(expand=True, side="bottom")

        self.label_rank = tk.Label(self.rank_frame, text="Voici le classement général du Cookie Clicker !", font=("Courier", 15), fg="black",bg="white")
        self.label_rank.pack(pady=10)

        self.listbox_scores = tk.Listbox(self.rank_frame,  width=50, height=20)
        self.listbox_scores.pack()

        self.update_scores_display()

    def save_score(self):
        name = self.app_instance.player_name
        self.score = self.stat_cookie
        self.scores.append((name, self.score))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.save_scores_to_file()
        if hasattr(self, 'listbox_scores') and self.listbox_scores.winfo_exists():
            self.update_scores_display()
        self.master.quit()

    def load_scores(self):
        try:
            with open("scores.txt", "r") as file:
                for line in file:
                    name, score = line.strip().split(": ")
                    self.scores.append((name, int(score)))
            self.scores.sort(key=lambda x: x[1], reverse=True)
        except FileNotFoundError:
            pass

    def save_scores_to_file(self):
        with open("scores.txt", "w") as file:
            for name, score in self.scores:
                file.write(f"{name}: {score}\n")

    def update_scores_display(self):
        if hasattr(self, 'listbox_scores'):
            self.listbox_scores.delete(0, tk.END)
            for name, score in self.scores:
                self.listbox_scores.insert(tk.END, f"{name}: {score}")


