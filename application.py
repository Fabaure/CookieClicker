from Cookie import Cookie
from Statistiques import Statistiques
from Minijeu import Minijeu
from Upgrade import Upgrade
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
from tkinter import messagebox


class Application:
    def __init__(self, master):
        self.master = master
        self.pages = {}
        self.statebuttonDark = False
        self.selected_music = "None"
        mixer.init()
        self.indice = 0
        self.running = False
        self.time = 0

    def MainMenu(self):
        self.menu_root = tk.Toplevel()
        self.menu_root.geometry("1280x720")
        self.menu_root.title("Cookie Clicker")
        self.bg = "#effaff"
        self.menu_root.configure(bg=self.bg)

        self.img_logo = Image.open("LogoCookieClicker.png")
        self.img_logo = self.img_logo.resize((300, 300))
        self.logo = ImageTk.PhotoImage(self.img_logo)
        self.label_logo = tk.Label(self.menu_root, image=self.logo, bg=self.bg)
        self.label_logo.pack()

        self.frame_bottom = tk.Frame(self.menu_root, highlightthickness=0, bg=self.bg, width=400, height=100)
        self.frame_bottom.pack(expand=True)

        self.btn_jouer = tk.Button(self.frame_bottom, text="Jouer", font=("Comic Sans Ms", 25),
                                   command=lambda: [self.menu_root.destroy(), self.open_player_name_window()], width=8)
        self.btn_jouer.pack(pady=10)

        self.btn_option = tk.Button(self.frame_bottom, text="Options", font=("Comic Sans Ms", 25),
                                    command=self.create_options, highlightthickness=0, width=8)
        self.btn_option.pack(pady=10)

        self.btn_quitter = tk.Button(self.frame_bottom, text="Quitter", font=("Comic Sans Ms", 25),
                                     command=self.master.destroy, width=8)
        self.btn_quitter.pack(pady=10)

    # OPTION EN COURS
    def create_options(self):

        self.options_window = tk.Toplevel()
        self.options_window.title("Options")
        self.options_window.configure(bg=self.bg)

        # MUSIQUE
        self.label_music = tk.Label(self.options_window, text="Choisir la musique OST:")
        self.label_music.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.music_options = ["Musique 1", "Musique 2", "Musique 3"]
        self.music_dropdown = ttk.Combobox(self.options_window, values=self.music_options)
        self.music_dropdown.set(self.selected_music)
        self.musicchoose = self.music_dropdown.get
        print(self.musicchoose)
        self.music_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # VOLUME
        self.label_volume = tk.Label(self.options_window, text="Volume:")
        self.label_volume.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.volume_scale = tk.Scale(self.options_window, from_=0, to=100, orient="horizontal")
        self.volume_scale.set(50)
        self.volume_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # MODE NUIT
        self.dark_mode_var = tk.BooleanVar()
        self.dark_mode_var.set(self.statebuttonDark)
        self.dark_mode_button = tk.Checkbutton(self.options_window, text="Mode Sombre", variable=self.dark_mode_var,
                                               command=lambda: self.update_background_color(self.dark_mode_var))
        self.dark_mode_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="w")

        self.button_frame = tk.Frame(self.options_window, bg=self.bg)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        self.close_button = tk.Button(self.button_frame, text="Fermer", command=self.options_window.destroy)
        self.close_button.pack(side="left", padx=5)

        self.apply_button = tk.Button(self.button_frame, text="Appliquer", command=self.apply_music)
        self.apply_button.pack(side="left", padx=5)

    def apply_music(self):
        self.selected_music = self.music_dropdown.get()
        if self.selected_music == "Musique 1":
            self.selected_music = "Musique 1"
            mixer.music.load(f"Musique1.mp3")
            self.selected_music = "Musique 1"
            mixer.music.set_volume(self.volume_scale.get() / 100)
            mixer.music.play(-1)
        if self.selected_music == "Musique 2":
            self.selected_music = "Musique 1"
            # mixer.music.load(f"Musique2.mp3")
            self.selected_music = "Musique 2"
            # mixer.music.set_volume(self.volume_scale.get() / 100)
            # mixer.music.play(-1)
        elif self.selected_music == "Musique 3":
            self.selected_music = "Musique 3"
            # mixer.music.load(f"Musique3.mp3")
            self.selected_music = "Musique 3"
            # mixer.music.set_volume(self.volume_scale.get() / 100)
            # mixer.music.play(-1)

    def open_player_name_window(self):
        self.master.withdraw()  # Masquer la fenêtre principale
        self.player_name_window = tk.Toplevel(self.master)
        self.player_name_window.title("Entrez votre pseudo")
        self.player_name_window.protocol("WM_DELETE_WINDOW", self.cancel_name_entry)  # Définir une fonction pour intercepter la fermeture de la fenêtre

        self.label_name = tk.Label(self.player_name_window, text="Entrez votre pseudo:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.player_name_window)
        self.entry_name.pack(pady=10)

        self.button_confirm = tk.Button(self.player_name_window, text="Confirmer", command=self.test_name)
        self.button_confirm.pack(pady=10)

    def cancel_name_entry(self):
        messagebox.showwarning("Attention", "Veuillez entrer un pseudo pour commencer à jouer.")

    def test_name(self):
        if self.entry_name.get() == '':
            messagebox.showwarning("Attention", "Veuillez entrer un pseudo pour commencer à jouer.")
        else:
            self.player_name = self.entry_name.get()
            self.affichage_principale()
            self.start_game()
            self.player_name_window.destroy()

    def affichage_principale(self):
        self.master.deiconify()
        self.create_navigation_bar()
        self.create_pages()
        self.master.title("Cookie Clicker")
        self.indice = 1


    def update_time(self):
        if self.running:
            self.time += 1
            formatted_time = self.format_time(self.time)
            self.stat_instance.time_label.config(text=f"Temps de jeu: {formatted_time}")
            self.master.after(1000, self.update_time)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"

    def start_game(self):
        if not self.running:
            self.running = True
            self.update_time()

    def create_navigation_bar(self):
        self.navigation_frame = tk.Frame(self.master, bg="#E2BFB3", relief=tk.SUNKEN)
        self.navigation_frame.pack(side="top", fill="x")

        buttons = [("Cookie", lambda: self.show_page("Cookie")),
                   ("Boutique", lambda: self.show_page("Boutique")),
                   ("Mini-Jeu", lambda: self.show_page("Mini-Jeu")),
                   ("Statistiques", lambda: self.show_page("Statistiques"))]

        for text, command in buttons:
            self.button = tk.Button(self.navigation_frame, text=text, command=command, font=("Helvetica", 14), height=2,
                                    width=15)
            self.button.pack(side="left", padx=20, pady=10)

        self.button_quit = tk.Button(self.navigation_frame, text="Quitter", command= self.save_and_quit,
                                     font=("Helvetica", 14),
                                     height=2, width=15)
        self.button_quit.pack(side="right", padx=20, pady=10)

        self.option = tk.Button(self.navigation_frame, text="Options", command=self.create_options,
                                font=("Helvetica", 14),
                                height=2, width=15)
        self.option.pack(side="right", padx=20, pady=10)

    def save_and_quit(self):
            if hasattr(self, 'stat_instance'):
                self.stat_instance.save_score()
            self.master.quit()

    def create_pages(self):
        for page_name in ["Cookie", "Boutique", "Mini-Jeu", "Statistiques"]:
            self.page = tk.Frame(self.master, bg="white")
            self.page.pack(fill="both", expand=True)
            self.pages[page_name] = self.page
            self.label = tk.Label(self.page, text=page_name, font=("Helvetica", 18))
            self.label.pack(pady=50)

        # ICI POUR DEFINIR LES PAGES

        # =*=

        self.statistiques_page = self.pages["Statistiques"]
        self.stat_instance = Statistiques(self.statistiques_page, self)

        self.cookie_page = self.pages["Cookie"]
        self.cookie_instance = Cookie(self.cookie_page, self.stat_instance, self)

        self.boutique_page = self.pages["Boutique"]
        self.boutique = Upgrade(self.boutique_page, self.cookie_instance, self.stat_instance, self)

        self.minijeu_page = self.pages["Mini-Jeu"]
        self.minijeu = Minijeu(self.minijeu_page, self.cookie_instance, self.stat_instance, self)

        # =*=

        self.show_page("Cookie")

    def show_page(self, page_name):
        for self.page in self.pages.values():
            self.page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

    def update_background_color(self, dark_mode_var):
        if self.indice == 0:

            if dark_mode_var.get():
                self.statebuttonDark = True
                self.bg = "#212121"
            else:
                self.statebuttonDark = False
                self.bg = "#effaff"
            self.menu_root.configure(bg=self.bg)
            self.frame_bottom.configure(bg=self.bg)
            self.label_logo.configure(bg=self.bg)
            self.options_window.configure(bg=self.bg)
            self.button_frame.configure(bg=self.bg)
        else:
            if dark_mode_var.get():
                self.statebuttonDark = True
                self.bg = "#212121"
            else:
                self.statebuttonDark = False
                self.bg = "#effaff"
            for pages_name in ["Cookie", "Boutique", "Mini-Jeu", "Statistiques"]:
                self.pageBG = self.pages[pages_name]
                self.pageBG.configure(bg=self.bg)
            self.options_window.configure(bg=self.bg)
            self.button_frame.configure(bg=self.bg)

    def display_message(self, message):
        dialogue_frame = tk.Frame(self.master, bg="white", bd=2, relief=tk.SOLID)
        dialogue_frame.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

        dialogue_label = tk.Label(dialogue_frame, text=message, justify="center", wraplength=600, bg="white",
                                  font=("Helvetica", 10))
        dialogue_label.pack(padx=10, pady=10)

        self.master.after(5000, dialogue_frame.destroy)
