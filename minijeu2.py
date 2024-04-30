import tkinter as tk
from tkinter import PhotoImage


class Minijeu2:

    def __init__(self, master):
        self.master = master
        self.master.title("Sauve ton cookie!")
        self.master.geometry("600x600")

        self.cookies = 0
        self.game_started = False
        self.create_widgets()

    def create_widgets(self):

        side_frame = tk.Frame(self.master)
        side_frame.pack(side="top", padx=10)

        rules_text = ( "Bonjour et bienvenue à notre deuxième mini-jeu !"
"\n Dans celui-ci, la rapidité est la clé, alors soyez vif et ne vous trompez pas. "
"\n Défendez votre cookie de macaron le glouton en cliquant sur lui lorsqu'il apparait. "
"\nSi vous le ratez vous perdez 1 vie "
"\n Attention ne cliquer pas lorsqu'il n'est pas là vous perderez 1 vie."
"\n Vous avez 2 vies, essayer de les conserver."
"\n Soyez précis et tentez de décrocher les meilleures récompenses ! "
"\n Appuyez sur 'Start' pour commencer !")
        rules_label = tk.Label(side_frame, text=rules_text, justify= "center")
        rules_label.pack(side="top", pady=20)

        self.vies_label = tk.Label(self.master, text="Vies: 2")
        self.vies_label.pack(pady=10)

        self.start_image = PhotoImage(file="bouton.png").subsample(3, 3)
        self.start_button = tk.Button(self.master, image=self.start_image, command=self.start_game, borderwidth=0)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="")
        self.timer_label.pack(pady=10)

        self.cookie_image = PhotoImage(file="cookie.png").subsample(3, 3)
        self.cookie_label = tk.Label(self.master, image=self.cookie_image, borderwidth=0)
        self.cookie_label.pack(pady=20, side="left", padx=30)

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.cookies = 0
            self.vies_label.config(text="Vies: 2")
            self.start_button.pack_forget()
            self.timer_label.pack()
            self.countdown(60)

    def countdown(self, count):
        if count >= 0:
            self.timer_label.config(text="Temps restant: " + str(count))
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.end_game()

    def end_game(self):
        self.game_started = False
        self.start_button.pack_forget()
        self.timer_label.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = Minijeu2(root)
    root.mainloop()