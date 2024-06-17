from Cookie import Cookie
from Statistiques import Statistiques
from Minijeu import Minijeu
from Upgrade import Upgrade
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk  # Gestion d'images
from pygame import mixer  # Gestion de musique
from tkinter import messagebox  # Gestion des boîtes de dialogue

class Application:
    def __init__(self, master):
        # Initialisation de l'application
        self.master = master
        self.pages = {}  # Dictionnaire pour stocker les différentes pages de l'application
        self.statebuttonDark = False  # État du mode sombre
        self.selected_music = "None"
        mixer.init()  # Initialise la lecture audio de pygame
        self.running = False  # État du jeu
        # Initialisations à 0
        self.indice = 0
        self.running = False
        self.time = 0
        self.bg_main = "white"
        self.bg_bar = "#F1C8E1"
        self.font = "black"
        self.label_titles = {}

    def MainMenu(self):
        # Méthode pour créer le menu principal de l'application
        self.menu_root = tk.Toplevel()  # Crée une fenêtre
        self.menu_root.geometry("1280x720")  # Définit sa taille
        self.menu_root.title("Cookie Clicker")  # Définit son titre
        self.bg = "#effaff"  # Couleur de fond
        self.menu_root.configure(bg=self.bg)

        # Chargement du logo Cookie Clicker
        self.img_logo = Image.open("Assets/Images/LogoCookieClicker.png")
        self.img_logo = self.img_logo.resize((300, 300))
        self.logo = ImageTk.PhotoImage(self.img_logo)
        self.label_logo = tk.Label(self.menu_root, image=self.logo, bg=self.bg)
        self.label_logo.pack()

        # Cadre avec les boutons
        self.frame_bottom = tk.Frame(self.menu_root, highlightthickness=0, bg=self.bg, width=400, height=100)
        self.frame_bottom.pack(expand=True)

        # Bouton Jouer
        self.btn_jouer = tk.Button(self.frame_bottom, text="Jouer", font=("Comic Sans Ms", 25),
                                   command=lambda: [self.menu_root.destroy(), self.open_player_name_window()], width=8)
        self.btn_jouer.pack(pady=10)

        # Bouton Options
        self.btn_option = tk.Button(self.frame_bottom, text="Options", font=("Comic Sans Ms", 25),
                                    command=self.create_options, highlightthickness=0, width=8)
        self.btn_option.pack(pady=10)

        # Bouton Quitter
        self.btn_quitter = tk.Button(self.frame_bottom, text="Quitter", font=("Comic Sans Ms", 25),
                                     command=self.master.destroy, width=8)
        self.btn_quitter.pack(pady=10)

    def create_options(self):
        # Méthode pour créer la fenêtre des options
        self.options_window = tk.Toplevel()
        self.options_window.title("Options")
        self.options_window.configure(bg=self.bg)

        # Label pour choisir la musique
        self.label_music = tk.Label(self.options_window, text="Choisir la musique OST:")
        self.label_music.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.music_options = ["Musique 1", "Musique 2", "Musique 3"]
        self.music_dropdown = ttk.Combobox(self.options_window, values=self.music_options)
        self.music_dropdown.set(self.selected_music)
        self.music_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Label et échelle pour le volume
        self.label_volume = tk.Label(self.options_window, text="Volume:")
        self.label_volume.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.volume_scale = tk.Scale(self.options_window, from_=0, to=100, orient="horizontal")
        self.volume_scale.set(50)
        self.volume_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Case à cocher pour le mode sombre
        self.dark_mode_var = tk.BooleanVar()
        self.dark_mode_var.set(self.statebuttonDark)
        self.dark_mode_button = tk.Checkbutton(self.options_window, text="Mode Sombre", variable=self.dark_mode_var,
                                               command=lambda: self.update_background_color(self.dark_mode_var))
        self.dark_mode_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="w")

        # Cadre pour les boutons de contrôle
        self.button_frame = tk.Frame(self.options_window, bg=self.bg)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        # Bouton Fermer
        self.close_button = tk.Button(self.button_frame, text="Fermer", command=self.options_window.destroy)
        self.close_button.pack(side="left", padx=5)

        # Bouton Appliquer
        self.apply_button = tk.Button(self.button_frame, text="Appliquer", command=self.apply_music)
        self.apply_button.pack(side="left", padx=5)

    def apply_music(self):
        # Méthode pour mettre la musique
        self.selected_music = self.music_dropdown.get()

        if self.selected_music == "Musique 1":
            # Charge et joue la première musique selon volume
            mixer.music.load(f"Assets/Musiques/Musique1.mp3")
            mixer.music.set_volume(self.volume_scale.get() / 100)
            mixer.music.play(-1)
        elif self.selected_music == "Musique 2":
            # Charge et joue la deuxième musique selon volume
            mixer.music.load(f"Assets/Musiques/Musique2.mp3")
            mixer.music.set_volume(self.volume_scale.get() / 100)
            mixer.music.play(-1)
        elif self.selected_music == "Musique 3":
            # Charge et joue la troisième musique selon volume
            mixer.music.load(f"Assets/Musiques/Musique3.mp3")
            mixer.music.set_volume(self.volume_scale.get() / 100)
            mixer.music.play(-1)

    def open_player_name_window(self):
        # Méthode pour ouvrir la fenêtre d'entrée du pseudo du joueur
        self.master.withdraw()  # Masque la fenêtre principale
        self.player_name_window = tk.Toplevel(self.master)
        self.player_name_window.title("Entrez votre pseudo")
        self.player_name_window.protocol("WM_DELETE_WINDOW", self.cancel_name_entry)

        self.label_name = tk.Label(self.player_name_window, text="Entrez votre pseudo:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.player_name_window)
        self.entry_name.pack(pady=10)

        self.button_confirm = tk.Button(self.player_name_window, text="Confirmer", command=self.test_name)
        self.button_confirm.pack(pady=10)

    def cancel_name_entry(self):
        # Méthode pour afficher un avertissement si aucun pseudo n'est entré
        messagebox.showwarning("Attention", "Veuillez entrer un pseudo pour commencer à jouer.")

    def test_name(self):
        # Méthode pour vérifier et utiliser le pseudo entré par le joueur
        if self.entry_name.get() == '':
            messagebox.showwarning("Attention", "Veuillez entrer un pseudo pour commencer à jouer.")
        else:
            self.player_name = self.entry_name.get()
            self.affichage_principale()
            self.start_game()
            self.player_name_window.destroy()

    def affichage_principale(self):
        # Méthode pour afficher l'interface principale du jeu
        self.master.deiconify()
        self.create_navigation_bar()  # Crée la barre de navigation en haut
        self.create_pages()  # Crée les différentes pages de l'application
        self.master.title("Cookie Clicker")
        self.indice = 1  # Indice pour suivre l'état de l'application

    def update_time(self):
        # Méthode pour mettre à jour le temps de jeu
        if self.running:
            self.time += 1  # Incrémente le temps de jeu en secondes
            formatted_time = self.format_time(self.time)  # Formate le temps sous forme HH:MM:SS
            self.stat_instance.time_label.config(
                text=f"Temps de jeu: {formatted_time}")  # Met à jour l'affichage du temps de jeu
            self.master.after(1000, self.update_time)  # Attend 1 seconde et refait

    def format_time(self, seconds):
        # Méthode pour formater le temps en heures, minutes, secondes
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"

    def start_game(self):
        # Méthode pour démarrer le jeu
        if not self.running:
            self.running = True
            self.update_time()

    def create_navigation_bar(self):
        # Méthode pour créer la barre de navigation en haut de l'interface
        self.navigation_frame = tk.Frame(self.master, bg=self.bg_bar, relief=tk.SUNKEN)
        self.navigation_frame = tk.Frame(self.master, bg="#E2BFB3", relief=tk.SUNKEN)
        self.navigation_frame.pack(side="top", fill="x")
        # Liste des boutons de navigation
        buttons = [("Cookie", lambda: self.show_page("Cookie")),
                   ("Boutique", lambda: self.show_page("Boutique")),
                   ("Mini-Jeu", lambda: self.show_page("Mini-Jeu")),
                   ("Statistiques", lambda: self.show_page("Statistiques"))]

        # Crée chaque bouton dans la barre de navigation
        for text, command in buttons:
            self.button = tk.Button(self.navigation_frame, text=text, command=command, font=("Helvetica", 14), height=2,
                                    width=15)
            self.button.pack(side="left", padx=20, pady=10)

        # Bouton Quitter
        self.button_quit = tk.Button(self.navigation_frame, text="Quitter", command=self.save_and_quit,
                                     font=("Helvetica", 14),
                                     height=2, width=15)
        self.button_quit.pack(side="right", padx=20, pady=10)

        # Bouton Options
        self.option = tk.Button(self.navigation_frame, text="Options", command=self.create_options,
                                font=("Helvetica", 14),
                                height=2, width=15)
        self.option.pack(side="right", padx=20, pady=10)

    def save_and_quit(self):
        # Méthode pour sauvegarder les scores et quitter l'application
        if hasattr(self, 'stat_instance'):
            self.stat_instance.save_score()
            self.master.quit()

    def create_pages(self):
        self.custom_fontCookie = font.Font(family="Cookies", size=100)
        self.custom_fontOther = font.Font(family="Cookies", size=60)
        # Méthode pour créer les différentes pages de l'application
        for page_name in ["Cookie", "Boutique", "Mini-Jeu", "Statistiques"]:
            self.page = tk.Frame(self.master, bg=self.bg_main)
            self.page.pack(fill="both", expand=True)
            self.pages[page_name] = self.page
            if page_name == "Cookie":
                self.labelTitle = tk.Label(self.page, text=page_name, font=self.custom_fontCookie, bg=self.bg_main, fg ="#825D46")
            else:
                self.labelTitle = tk.Label(self.page, text=page_name, font=self.custom_fontOther, bg=self.bg_main, fg="#825D46")
            self.labelTitle.pack(pady=50)
            self.label_titles[page_name] = self.labelTitle

        # Crée les instances des différentes pages avec les classes associées
        self.statistiques_page = self.pages["Statistiques"]
        self.stat_instance = Statistiques(self.statistiques_page, self)

        self.cookie_page = self.pages["Cookie"]
        self.cookie_instance = Cookie(self.cookie_page, self.stat_instance, self)

        self.boutique_page = self.pages["Boutique"]
        self.boutique = Upgrade(self.boutique_page, self.cookie_instance, self.stat_instance, self)

        self.minijeu_page = self.pages["Mini-Jeu"]
        self.minijeu = Minijeu(self.minijeu_page, self.cookie_instance, self.stat_instance, self)

        # Affiche la page "Cookie" par défaut au lancement de l'application
        self.show_page("Cookie")

    def show_page(self, page_name):
        # Méthode pour afficher une page spécifique et masquer les autres
        for self.page in self.pages.values():
            self.page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

    def update_background_color(self, dark_mode_var):
        # Méthode pour mettre à jour la couleur de fond en fonction du mode sombre ou clair
        if self.indice == 0:  # Si l'application est au menu principal
            if dark_mode_var.get():
                self.statebuttonDark = True
                self.bg = "#212121"
            else:
                self.statebuttonDark = False
                self.bg = "#effaff"
            # Met à jour la couleur de fond pour les différents éléments du menu principal
            self.menu_root.configure(bg=self.bg)
            self.frame_bottom.configure(bg=self.bg)
            self.label_logo.configure(bg=self.bg)
            self.options_window.configure(bg=self.bg)
            self.button_frame.configure(bg=self.bg)
        else:  # Si l'application est sur une des pages du jeu
            if dark_mode_var.get():
                self.statebuttonDark = True
                self.bg_main = "#212121"
                self.bg_bar = "#A2739B"
                self.font = "white"
                self.fontUpgrade = "white"
            else:
                self.statebuttonDark = False
                self.bg_main = "white"
                self.bg_bar = "#F1C8E1"
                self.font="black"
                self.fontUpgrade ="#612E18"

            #Update Main
            self.navigation_frame.configure(bg=self.bg_bar)
            for page_name, page_frame in self.pages.items():
                page_frame.configure(bg=self.bg_main)
                label_title = self.label_titles[page_name]
                label_title.configure(bg=self.bg_main)
            self.options_window.configure(bg=self.bg_main)
            self.button_frame.configure(bg=self.bg_main)

            # Update Cookie
            self.cookie_instance.cookie_frame.configure(bg=self.bg_main)
            self.cookie_instance.label_cookie_count.configure(bg=self.bg_main, fg=self.font)
            self.cookie_instance.cookie_button.configure(bg=self.bg_main)

            # Update Statistique
            self.stat_instance.stat_frame.configure(bg=self.bg_main)
            self.stat_instance.time_label.configure(fg=self.font, bg=self.bg_main)
            self.stat_instance.label_title.configure(fg=self.font, bg=self.bg_main)
            self.stat_instance.label_clique_nbr.configure(fg=self.font,bg=self.bg_main)
            self.stat_instance.label_cookie_nbr.configure(fg=self.font,bg=self.bg_main)
            self.stat_instance.label_record_mn1.configure(fg=self.font,bg=self.bg_main)
            self.stat_instance.label_record_mn2.configure(fg=self.font,bg=self.bg_main)
            self.stat_instance.label_record_mn3.configure(fg=self.font,bg=self.bg_main)
            self.stat_instance.rank_frame.configure(bg=self.bg_main)
            self.stat_instance.label_rank.configure(fg=self.font, bg=self.bg_main)

            # Update MiniJeu
            self.minijeu.minijeu_frame.configure(bg=self.bg_main)
            self.minijeu.magical_button.configure(bg=self.bg_main,activebackground=self.bg_main)

            #Update Boutique
            self.boutique.upgrade_frame.configure(bg=self.bg_main)
            self.boutique.title_label.configure(bg=self.bg_main)
            for button in [self.boutique.upgrade_button1, self.boutique.upgrade_button2, self.boutique.upgrade_button3, self.boutique.upgrade_button4]:
                button.configure(bg=self.bg_main)
            for level in [self.boutique.level_label1, self.boutique.level_label2, self.boutique.level_label3, self.boutique.level_label4]:
                level.configure(fg=self.fontUpgrade)
            for label in [self.boutique.level_label1, self.boutique.level_label2, self.boutique.level_label3, self.boutique.level_label4]:
                label.configure(bg=self.bg_main)

            for avatar_button in [self.boutique.avatar0_button, self.boutique.avatar1_button, self.boutique.avatar2_button, self.boutique.avatar3_button,
                                  self.boutique.avatar4_button]:
                avatar_button.configure(bg=self.bg_main)
            self.boutique.magical_button.configure(bg=self.bg_main)

    def display_message(self, message):
        # Méthode pour afficher un message temporaire à l'utilisateur
        dialogue_frame = tk.Frame(self.master, bg="white", bd=2, relief=tk.SOLID)
        dialogue_frame.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

        dialogue_label = tk.Label(dialogue_frame, text=message, justify="center", wraplength=600, bg="white",
                                  font=("Helvetica", 10))
        dialogue_label.pack(padx=10, pady=10)

        self.master.after(5000, dialogue_frame.destroy)  # Détruit le message après 5 secondes
