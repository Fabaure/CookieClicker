from Cookie import Cookie
from Statistiques import Statistiques
from Minijeu import Minijeu
from Upgrade import Upgrade
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Application:
    def __init__(self, master):
        self.master = master
        self.pages = {}
        self.image_fond = None
        self.image_secondaire = None
        self.frame_options = None

    def MainMenu(self):
        self.menu_root = tk.Toplevel()
        self.menu_root.geometry("1280x720")
        self.menu_root.title("Cookie Clicker")
        self.bg="#effaff"
        self.menu_root.configure(bg=self.bg)

        self.img_logo = Image.open("LogoCookieClicker.png")
        self.img_logo = self.img_logo.resize((300, 300))
        self.logo = ImageTk.PhotoImage(self.img_logo)
        self.label_logo = tk.Label(self.menu_root, image=self.logo, bg=self.bg)
        self.label_logo.pack()

        self.frame_bottom = tk.Frame(self.menu_root, highlightthickness=0, bg=self.bg, width=400, height=100)
        self.frame_bottom.pack(expand=True)

        self.btn_jouer = tk.Button(self.frame_bottom, text="Jouer", font=("Comic Sans Ms", 25), command=lambda: [self.menu_root.destroy(), self.affichage_principale()], width=8)
        self.btn_jouer.pack(pady=10)

        self.btn_option = tk.Button(self.frame_bottom, text="Options", font=("Comic Sans Ms", 25), highlightthickness=0, width=8)
        self.btn_option.pack(pady=10)

        self.btn_quitter = tk.Button(self.frame_bottom, text="Quitter", font=("Comic Sans Ms", 25),command=self.master.destroy, width=8)
        self.btn_quitter.pack(pady=10)

#OPTION EN COURS
    '''
    def create_options(self):

        options_window = tk.Toplevel(self.master)
        options_window.title("Options")
        options_window.configure(bg="#effaff")

        #MUSIQUE
        label_music = tk.Label(options_window, text="Choisir la musique OST:")
        label_music.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        selected_music = tk.StringVar()
        selected_music.set("Musique 1")
        music_options = ["Musique 1", "Musique 2", "Musique 3"]
        music_dropdown = ttk.Combobox(options_window, textvariable=selected_music, values=music_options)
        music_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        #VOLUME
        label_volume = tk.Label(options_window, text="Volume:")
        label_volume.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        volume_scale = tk.Scale(options_window, from_=0, to=100, orient="horizontal")
        volume_scale.set(50)
        volume_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        #MODE NUIT
        dark_mode_var = tk.BooleanVar()
        dark_mode_var.set(False)
        dark_mode_button = tk.Checkbutton(options_window, text="Mode Sombre", variable=dark_mode_var, command=lambda: self.update_background_color(options_window, dark_mode_var))
        dark_mode_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="w")

        close_button = tk.Button(options_window, text="Fermer", command=options_window.destroy)
        close_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="e")
    

    def update_background_color(self, dark_mode_var):
        if dark_mode_var.get():
            self.menu_root.configure(bg="#212121")
            self.frame_bottom.configure(bg="#212121")
            self.label_logo.configure(bg="#212121")

        else:
            self.menu_root.configure(bg="#effaff")
            self.frame_bottom.configure(bg="#effaff")
            self.label_logo.configure(bg="#effaff")
    '''
    def affichage_principale(self):
        self.master.deiconify()
        self.create_navigation_bar()
        self.create_pages()
        self.master.title("Navigation Bar")

    def create_navigation_bar(self):
        navigation_frame = tk.Frame(self.master, bg="#E2BFB3", relief=tk.SUNKEN)
        navigation_frame.pack(side="top", fill="x")

        buttons = [("Cookie", lambda: self.show_page("Cookie")),
                   ("Boutique", lambda: self.show_page("Boutique")),
                   ("Mini-Jeu", lambda: self.show_page("Mini-Jeu")),
                   ("Statistiques", lambda: self.show_page("Statistiques"))]

        for text, command in buttons:
            button = tk.Button(navigation_frame, text=text, command=command, font=("Helvetica", 14), height=2, width=15)
            button.pack(side="left", padx=20, pady=10)

        self.button_quit = tk.Button(navigation_frame, text="Quitter", command=self.master.quit, font=("Helvetica", 14),height=2, width=15)
        self.button_quit.pack(side="right", padx=20, pady=10)

    def create_pages(self):
        for page_name in ["Cookie", "Boutique", "Mini-Jeu", "Statistiques"]:
            page = tk.Frame(self.master, bg="white")
            page.pack(fill="both", expand=True)
            self.pages[page_name] = page
            label = tk.Label(page, text=page_name, font=("Helvetica", 18))
            label.pack(pady=50)

        # ICI POUR DEFINIR LES PAGES

        # =*=

        self.statistiques_page = self.pages["Statistiques"]
        self.stat_instance = Statistiques(self.statistiques_page)

        self.cookie_page = self.pages["Cookie"]
        self.cookie_instance = Cookie(self.cookie_page, self.stat_instance)

        self.boutique_page = self.pages["Boutique"]
        self.boutique = Upgrade(self.boutique_page, self.cookie_instance)

        self.minijeu_page = self.pages["Mini-Jeu"]
        self.minijeu = Minijeu(self.minijeu_page, self.cookie_instance, self.stat_instance)

        # =*=

        self.show_page("Cookie")

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)