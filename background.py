import tkinter as tk
from tkinter import PhotoImage
class Background:
    def __init__(self, master):
        self.master = master
        self.master.title("Cookie Clicker")
        self.master.geometry("1040x480")
        self.master.config(background='#5886e7')
