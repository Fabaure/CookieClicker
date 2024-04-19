import tkinter as tk
from Cookie import Cookie
from Upgrade import Upgrade
from Minijeu import Minijeu
from Statistiques import Statistiques

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Navigation Bar")

        #Méthode pour prendre les paramètre d'écran de l'ordinateur et prend 80%
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

        self.pages = {}
        self.create_navigation_bar()
        self.create_pages()

    def create_navigation_bar(self):
        navigation_frame = tk.Frame(self.master, bg="#E2BFB3", relief=tk.SUNKEN)
        navigation_frame.pack(side="top", fill="x")

        buttons = [("Cookie", lambda: self.show_page("Cookie")),
                   ("Boutique", lambda: self.show_page("Boutique")),
                   ("Mini-Jeu", lambda: self.show_page("Mini-Jeu")),
                   ("Statistiques", lambda: self.show_page("Statistiques"))]

        for text, command in buttons:
            button = tk.Button(navigation_frame, text=text, command=command, font=("Helvetica", 14), height=2, width=20)
            button.pack(side="left", padx=20, pady=10)

    def create_pages(self):
        for page_name in ["Cookie", "Boutique", "Mini-Jeu","Statistiques"]:
            page = tk.Frame(self.master, bg="white")
            page.pack(fill="both", expand=True)
            self.pages[page_name] = page
            label = tk.Label(page, text=page_name, font=("Helvetica", 18))
            label.pack(pady=30)

    # ICI POUR DEFINIR LES PAGES

    #=*=
        self.cookie_page = self.pages["Cookie"]
        self.cookie_instance = Cookie(self.cookie_page)

        self.boutique_page = self.pages["Boutique"]
        self.boutique = Upgrade(self.boutique_page, self.cookie_instance)

        self.minijeu_page = self.pages["Mini-Jeu"]
        self.minijeu = Minijeu(self.minijeu_page)

        self.statistiques_page = self.pages["Statistiques"]
        self.statistiques = Statistiques(self.statistiques_page)
    #=*=

        self.show_page("Cookie")
    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)