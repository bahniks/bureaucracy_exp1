#! python3
from tkinter import *
from tkinter import ttk

from itertools import chain

import os
import random

from common import ExperimentFrame, InstructionsFrame
from gui import GUI


################################################################################
# TEXTS


instructions = """V následující části experimentu je vaším úkolem odhadovat pravděpodobnosti různých jevů.
Pokud se vám bude zdát, že nemáte dostatek informací, zkuste přesto uvést váš nejlepší odhad dané pravděpodobnosti.
I pokud se vám budou zdát zadání podobná, čtěte je pečlivě, mohou mít pouze malé odlišnosti, které však mohou ovlivnit váš odhad pravděpodobnosti.

Odpovědi se zadávají pomocí šoupátka (slider). Před pokračováním musíte s šoupátkem pohnout, ale to neznamená, že nemůžete odpovědět pravděpodobnost 0 %.

Pro započetí úkolu klikněte na tlačítko 'Pokračovat'.
"""



keys = []
materials = {}
with open(os.path.join(os.path.dirname(__file__), "wee.txt"), encoding = "utf-8") as file:
    for i, line in enumerate(file):
        if not line.strip():
            continue
        if i % 6 == 0:
            key = line.strip()
            keys.append(key)
            materials[key] = []
        else:
            materials[key].append(line.strip())        

random.shuffle(keys)
conditionNames = ["Marginal", "Conditional", "Diagnostic", "Causal"]


################################################################################


class WeakEvidence(ExperimentFrame):
    def __init__(self, root):
        super().__init__(root)

        self.numberOfRounds = min([10, len(materials)])
        self.conditions = [0]*int(self.numberOfRounds/2) + [1]*int(self.numberOfRounds/2)
        random.shuffle(self.conditions)
        self.conditions = list(chain(*zip(self.conditions, [2]*self.numberOfRounds)))
        self.conditions += [3]*self.numberOfRounds
        self.keys = list(chain(*[(key, key) for key in keys[:self.numberOfRounds]])) + keys[:self.numberOfRounds]

        self.file.write("Weak evidence\n")

        self.answerVar = IntVar()
        self.answerVar.set(0)

        self.round = 0

        self.text = Text(self, font = "helvetica 18", relief = "flat", background = "white", height = 4,
                         wrap = "word", highlightbackground = "white", width = 80)
        self.text.grid(row = 1, column = 1)
        self.showText()

        ttk.Style().configure("TScale", background = "white")

        self.scale = ttk.Scale(self, orient = HORIZONTAL, from_ = 0, to = 100,
                               variable = self.answerVar, command = self.changedScale)
        self.scale.grid(row = 2, column = 1, sticky = EW)

        self.percents = ttk.Label(self, text = "0%", background = "white",
                                   font = "helvetica 18")
        self.percents.grid(row = 3, column = 1)     

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(0, weight = 3)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(6, weight = 3)

        ttk.Style().configure("TButton", font = "helvetica 18")
        self.next = ttk.Button(self, text = "Pokračovat", command = self.proceed, state = "disabled")
        self.next.grid(row = 5, column = 0, columnspan = 4, pady = 15)
        

    def changedScale(self, value):
        self.answerVar.set(round(self.answerVar.get(), 1))
        self.percents["text"] = "{}%".format(self.answerVar.get())
        self.next["state"] = "!disabled"


    def showText(self):
        self.text.config(state = "normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", materials[self.keys[self.round]][self.conditions[self.round]])
        self.text.config(state = "disabled")


    def proceed(self):
        self.write()
        self.round += 1
        if self.round == self.numberOfRounds*3:
            self.nextFun()
        else:
            self.answerVar.set(0)
            self.next["state"] = "disabled"
            self.showText()
            self.percents["text"] = "{}%".format(self.answerVar.get())            


    def write(self):
        if self.round == self.numberOfRounds*3:
            return
        self.file.write("\t".join([self.id, str(self.round + 1), self.keys[self.round], conditionNames[self.conditions[self.round]],
                                   str(self.answerVar.get())]) + "\n")



WeakEvidenceInstructions = (InstructionsFrame, {"text": instructions, "height": 11, "font": 18, "width": 80})




if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([WeakEvidenceInstructions,
         WeakEvidence])
