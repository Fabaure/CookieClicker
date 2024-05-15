import tkinter as tk
from tkinter import PhotoImage


class Minijeu3:

    def __init__(self, master):
        self.master = master
        self.master.title("Mange pépites!")
        self.master.geometry("900x600")
        self.choco = 0
        self.game_started = False

        self.create_widgets()

    def create_widgets(self):

        side_frame = tk.Frame(self.master)
        side_frame.pack(side="top", padx=10)

        rules_text = ( "Bonjour et bienvenue à notre troisième mini-jeu !\n Dans celui-ci, la rapidité est la clé, alors soyez vif et précis!"
"\n Vous disposez d'une minute pour cliquer sur toutes les pepites de chocolat qui apparaissent sur le cookie"
"\n Dans ce jeu, vous trouverez plusieurs niveaux qui montent en difficulté."
"\n Régalez vous et tentez de décrocher les meilleures récompenses ! "
"\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify="center")
        rules_label.pack(side="top", pady=20)

        self.choco_label = tk.Label(self.master, text="Pépites: 0")
        self.choco_label.pack(pady=10)


        self.cookie_image = PhotoImage(file="cookie_sans_pepite.png").subsample(2, 2)
        self.cookie_label = tk.Label(self.master, image=self.cookie_image, state="disabled", borderwidth=0)
        self.cookie_label.pack(pady=30)

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="")

    def click_pepite(self):
        if self.game_started:
            self.choco += 1
            self.choco_label.config(text="Pépites " + str(self.choco))

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.choco = 0
            self.choco_label.config(text="Pépites: 0")
            self.start_button.pack_forget()
            self.timer_label.pack()
            self.cookie_label.config(state="normal")
            self.countdown(30)

    def countdown(self, count):
        if count > 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.end_game()



    def end_game(self):
        self.game_started = False
        self.cookie_label.config(state="disabled")
        self.start_button.pack_forget()
        self.timer_label.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = Minijeu3(root)
    root.mainloop()