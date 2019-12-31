import tkinter
from tkinter import *
from tkinter import ttk
from screens import New_Game_Screen

class Main_Screen:
    def __init__(self, master):
        self.root = master
        self.root.title("Main Screen")
        self.title_lbl = ttk.Label(self.root, text="Welcome to Blackjack with statistics!")
        self.new_game_btn = ttk.Button(self.root, text="New Game")
        self.load_game_btn = ttk.Button(self.root, text="Load Game")
        self.leaderboard_btn = ttk.Button(self.root, text="Leaderboard")
        self.quit_btn = ttk.Button(self.root, text="Quit")

        self.new_game_btn.config(command=self.new_game)
        self.load_game_btn.config(command=self.load_game)
        self.leaderboard_btn.config(command=self.leaderboard)
        self.quit_btn.config(command=self.quit)

        self.title_lbl.pack()
        self.new_game_btn.pack()
        self.load_game_btn.pack()
        self.leaderboard_btn.pack()
        self.quit_btn.pack()

    def quit(self):
        self.root.destroy()
        quit()

    def new_game(self):
        self.root.destroy()
        self.root = Tk()
        New_Game_Screen.New_Game_Screen(self.root)

    def load_game(self):
        self.root.destroy()

    def leaderboard(self):
        self.root.destroy()
