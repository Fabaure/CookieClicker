import tkinter as tk
from tkinter import PhotoImage
import random

class Minijeu3:
    def __init__(self, master):
        self.master = master
        self.master.title("Mange pépites!")
        self.master.geometry("900x600")
        self.choco = 0
        self.game_started = False
        self.level = 1
        self.create_widgets()

    def create_widgets(self):
        side_frame = tk.Frame(self.master)
        side_frame.pack(side="top", padx=10)

        rules_text = ("Bonjour et bienvenue à notre troisième mini-jeu !\n Dans celui-ci, la rapidité est la clé, alors soyez vif et précis!"
                      "\n Vous disposez d'une minute pour cliquer sur toutes les pepites de chocolat qui apparaissent sur le cookie"
                      "\n Dans ce jeu, vous trouverez plusieurs niveaux qui montent en difficulté."
                      "\n Régalez vous et tentez de décrocher les meilleures récompenses ! "
                      "\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center")
        rules_label.pack(side="top", pady=20)

        self.choco_label = tk.Label(self.master, text="Pépites: 0")
        self.choco_label.pack(pady=10)

        self.niveau_label = tk.Label(self.master, text="Niveau: 0")
        self.niveau_label.pack(pady=10)

        self.cookie_image = PhotoImage(file="cookie_sans_pepite.png").subsample(2, 2)

        self.cookie_canvas = tk.Canvas(self.master, width=255, height=225)
        self.cookie_canvas.pack()
        self.cookie_canvas.create_image(0, 0, anchor=tk.NW, image=self.cookie_image)

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="")

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.level = 1
            self.choco = 0
            self.niveau_label.config(text="Niveau: 0")
            self.choco_label.config(text="Pépites: 0")
            self.start_button.pack_forget()
            self.timer_label.pack()
            self.countdown(30)
            self.niveau1()

    def create_multiple_chocolates(self, num_chocolates):
        self.clear_chocolates()
        self.chocolates = []
        for _ in range(num_chocolates):
            chocolate_id = self.create_chocolate()
            self.chocolates.append(chocolate_id)
            self.cookie_canvas.tag_bind(chocolate_id, "<Button-1>", self.click_chocolate)

    def create_chocolate(self):
        x = random.randint(50, 200)
        y = random.randint(50, 150)
        return self.cookie_canvas.create_oval(x, y, x + 20, y + 20, fill="#7C473B", outline="")

    def click_chocolate(self, event):
        self.choco += 1
        self.choco_label.config(text="Pépites: " + str(self.choco))
        self.cookie_canvas.delete(tk.CURRENT)
        if self.choco == 5:
            self.niveau2()
        elif self.choco == 15:
            self.niveau3()
        elif self.choco == 30:
            self.end_game()

    def countdown(self, count):
        if count > 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.end_game()


    def clear_chocolates(self):
        self.cookie_canvas.delete("all")
        self.cookie_canvas.create_image(0, 0, anchor=tk.NW, image=self.cookie_image)

    def niveau1(self):
        self.niveau_label.config(text="Niveau: 1")
        self.create_multiple_chocolates(5)

    def niveau2(self):
        self.niveau_label.config(text="Niveau: 2")
        self.create_multiple_chocolates(10)

    def niveau3(self):
        self.niveau_label.config(text="Niveau: 3")
        self.create_multiple_chocolates(15)

    def end_game(self):
        self.game_started = False
        self.timer_label.pack_forget()
        self.start_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = Minijeu3(root)
    root.mainloop()
