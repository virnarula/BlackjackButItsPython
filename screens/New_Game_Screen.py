from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model import *
from screens import Game_Screen

class New_Game_Screen:
    def __init__(self, master):
        self.root = master
        self.root.title("New Game")
        self.title_lbl = ttk.Label(self.root, text="Please enter your name:")
        self.text_field = Text(self.root, height=1, width=30)
        self.finish_btn = ttk.Button(self.root, text="Start Game")

        self.finish_btn.config(command=self.finish)

        self.title_lbl.pack()
        self.text_field.pack()
        self.finish_btn.pack()

    def finish(self):
        name = self.text_field.get(1.0, END)
        if name == "\n":
            messagebox.showwarning("Error", "You did not enter a name")
        else:
            game = Game(1, name)
            self.root.destroy()
            self.root = Tk()
            Game_Screen.Game_Screen(self.root, 1, game)



