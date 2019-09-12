#! python3
from tkinter import *
from tkinter import ttk

import os

from common import ExperimentFrame, InstructionsFrame, Question, Measure
from gui import GUI




class Debriefing(ExperimentFrame):
    def __init__(self, root):
        super().__init__(root)

        q1 = "Co si myslíte, že zkoumala studie s úlohou na třídění barevných geometrických tvarů?"
        self.question1 = Question(self, q1, width = 68, answer = (ttk.Entry, {"width": 118}))
        self.question1.grid(row = 1, column = 1, sticky = E)

        q2 = "Kdyby někdo ve snaze získat vepsané body navíc zatřídil tvar ke špatné\nbarvě a způsobil tak ztrátu bodů pro charitu, bylo by to:"
        adj1 = ["opovrženíhodné", "nespravedlivé", "nečestné", "nemorální"]
        self.frame1 = OneFrame(self, q2, adj1)
        self.frame1.grid(row = 2, column = 1, sticky = E)

        q3 = "Kdyby někdo ve snaze neztratit body pro charitu nezatřídil obrázek dle\ntvaru ale dle barvy a nezískal tak navíc body pro sebe, bylo by to:"
        adj2 = ["chvályhodné", "spravedlivé", "čestné", "morální"]
        self.frame2 = OneFrame(self, q3, adj2)
        self.frame2.grid(row = 3, column = 1, sticky = E)            

        ttk.Style().configure("TButton", font = "helvetica 15")
        self.next = ttk.Button(self, text = "Pokračovat", command = self.nextFun,
                               state = "disabled")
        self.next.grid(row = 4, column = 1, sticky = N)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 2)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(2, weight = 1)

    def check(self):
        if self.frame1.check() and self.frame2.check():
            self.next["state"] = "!disabled"
            return True


    def write(self):
        self.file.write("Dishonesty Questions\n" + self.id + "\t" + self.question1.answer.get() + "\t")
        self.frame1.write()
        self.file.write("\t")
        self.frame2.write()
        self.file.write("\n")



class OneFrame(Canvas):
    def __init__(self, root, question, adjectives):
        super().__init__(root, background = "white", highlightbackground = "white",
                         highlightcolor = "white")

        self.root = root
        self.file = self.root.file

        answers = ["určite ne", "spíše ne", "spíše ano", "určitě ano"]
        
        self.lab1 = ttk.Label(self, text = question, font = "helvetica 15", background = "white")
        self.lab1.grid(row = 2, column = 1, columnspan = 2, pady = 10, sticky = E)
        self.measures = []
        for count, word in enumerate(adjectives):
            self.measures.append(Measure(self, word, answers, "", "", function = self.root.check,
                                         labelPosition = "none"))
            self.measures[count].grid(row = count + 3, column = 1, columnspan = 2, sticky = E)

        self.frame = Canvas(self, background = "white", highlightbackground = "white",
                            highlightcolor = "white")
        self.frame.grid(column = 1, row = 7, columnspan = 2, pady = 20, sticky = E)
        
        self.comlab1 = ttk.Label(self.frame, text = "vlastní komentář:", font = "helvetica 14",
                                 background = "white")
        self.comlab1.grid(row = 7, column = 1, sticky = E)

        self.comVar = StringVar()
        self.comentry = ttk.Entry(self.frame, textvariable = self.comVar, width = 67)
        self.comentry.grid(row = 7, column = 2, sticky = W, padx = 50)


    def check(self):
        for measure in self.measures:
            if not measure.answer.get():
                return False
        else:
            return True             


    def write(self):
        for measure in self.measures:
            measure.write()
            self.file.write("\t")
        self.file.write(self.comVar.get())




if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Debriefing])

