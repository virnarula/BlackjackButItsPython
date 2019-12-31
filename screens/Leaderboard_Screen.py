from tkinter import *
from tkinter import ttk
from screens import Main_Screen


class Leaderboard_Screen:
    def __init__(self, master, games):
        self.root = master
        self.root.title("Leaderboard")
        self.games = games
        self.sortByScore()

        self.back_btn = ttk.Button(self.root, text="<-- Back")
        self.tree = ttk.Treeview(self.root)
        self.title_lbl = Label(self.root, text="Top winners")

        self.back_btn.config(command=self.back)
        self.populateTree()

        self.back_btn.pack()
        self.title_lbl.pack()
        self.tree.pack()

    def back(self):
        self.root.destroy()
        self.root = Tk()
        Main_Screen.Main_Screen(self.root)

    def sortByScore(self):
        for i in range(len(self.games)):
            max_idx = i
            for j in range(i + 1, len(self.games)):
                if self.games[j].money > self.games[max_idx].money:
                    max_idx = j
            temp = self.games[i]
            self.games[i] = self.games[max_idx]
            self.games[max_idx] = temp

    def populateTree(self):
        self.tree["columns"] = ("#1", "#2", "#3")
        self.tree.heading("#0", text="Rank")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Rounds Played")
        self.tree.heading("#3", text="Money")

        for i in range(len(self.games)):
            self.tree.insert("", i, "", text=str(i), values=(self.games[i].name, str(len(self.games[i].rounds)), str(self.games[i].money)))
