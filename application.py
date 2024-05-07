import tkinter as tk
from Cookie import Cookie
from Upgrade import Upgrade
from Minijeu import Minijeu
from Statistiques import Statistiques

class Application:
    def __init__(self, master):
        self.master = master
        self.pages = {}

    def Popup(self):
        popup = tk.Toplevel(self.master)
        popup.title("Bienvenue au jeu du Cookie Clicker")
        popup.geometry("500x200")
        self.label_rules = tk.Label(popup, text="Bonjour et bienvenue sur le jeu du Cookie Clicker !! ")
        self.label_rules.pack(padx=25)
        self.button_rules = tk.Button(popup, text="ok", anchor="center", command=lambda: [popup.destroy(), self.affichage_principale()], height=3, width=50, bg='#E2BFB3')
        self.button_rules.pack(anchor="center")

    def affichage_principale(self):

        # Méthode pour prendre les paramètre d'écran de l'ordinateur et prend 80%
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")


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

        self.statistiques_page = self.pages["Statistiques"]
        self.stat_instance = Statistiques(self.statistiques_page)

        self.cookie_page = self.pages["Cookie"]
        self.cookie_instance = Cookie(self.cookie_page, self.stat_instance)

        self.boutique_page = self.pages["Boutique"]
        self.boutique = Upgrade(self.boutique_page, self.cookie_instance)

        self.minijeu_page = self.pages["Mini-Jeu"]
        self.minijeu = Minijeu(self.minijeu_page, self.cookie_instance, self.stat_instance)

    #=*=

        self.show_page("Cookie")
    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)