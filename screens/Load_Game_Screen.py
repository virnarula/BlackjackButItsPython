from tkinter import *
from tkinter import ttk
from screens import Main_Screen


class Load_Game_Screen:
    def __init__(self, master, games):
        self.root = master
        self.root.title("Load Game")
        self.games = games

        self.back_btn = ttk.Button(self.root, text="<-- Back")
        self.combo_box = ttk.Combobox(self.root, values=self.generateComboVals())
        self.play_game_btn = ttk.Button(self.root, text="Play game")
        self.see_stats_btn = ttk.Button(self.root, text="See Stats")

        self.back_btn.config(command=self.back)
        self.play_game_btn.config(command=self.play_game)
        self.see_stats_btn.config(command=self.see_stats)

        self.back_btn.pack()
        self.combo_box.pack()
        self.play_game_btn.pack()
        self.see_stats_btn.pack()

    def back(self):
        self.root.destroy()
        self.root = Tk()
        Main_Screen.Main_Screen(self.root)

    def generateComboVals(self):
        vals = []
        for game in self.games:
            vals.append(game.name + " - " + str(game.money))
        return vals

    def play_game(self):
        1+1
    def see_stats(self):
        1+1
