# Importation de classes et de modules
import tkinter as tk
from tkinter import PhotoImage
from application import Application
from minijeu1 import Minijeu1

class CookieClickerApp:
    def __init__(self, master):
        # Initialisation des paramètres
        self.master = master
        self.master.geometry("1280x720")
        self.master.withdraw()
        self.application = Application(master)
        self.application.MainMenu()
        self.master.resizable(width=False, height=False)  # Empêche le redimensionnement de la fenêtre principale

if __name__ == "__main__":
    root = tk.Tk()  # Création de la fenêtre principale tkinter
    app = CookieClickerApp(root)  # Instanciation de l'application CookieClickerApp avec la fenêtre principale root
    root.mainloop()  # Boucle principale tkinter pour maintenir l'application en cours d'exécution
