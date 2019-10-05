#! python3
from tkinter import *
from tkinter import ttk
from collections import deque
from time import perf_counter, sleep

import random
import os

from common import ExperimentFrame, InstructionsFrame
from gui import GUI


items = [["subway", "vzdálenost stanic metra Muzeum a Hlavní nádraží"],
         ["soccer", "délka typického fotbalového hřiště"],
         ["tree", "nejvyšší strom světa"]]
random.shuffle(items)


class Comparison(ExperimentFrame):
    def __init__(self, root):
        super().__init__(root)

        self.file.write("Comparison\n")

        self.random = ttk.Button(self, text = "Znáhodnit", command = self.randomize)
        self.random.grid(row = 1, column = 1, columnspan = 2)

        self.slotwidth = 300
        self.slotheight = 150
        self.slot = Canvas(self, width = self.slotwidth+2, height = self.slotheight, background = "white",
                           highlightbackground = "black")
        self.slot.grid(row = 2, column = 1, columnspan = 2)

        self.slot.create_rectangle((3, 3, self.slotwidth/3 + 3, self.slotheight), width = 3)
        self.slot.create_rectangle((self.slotwidth/3 + 3, 3, 2*self.slotwidth/3 + 3, self.slotheight), width = 3)
        self.slot.create_rectangle((2*self.slotwidth/3 + 3, 3, self.slotwidth + 3, self.slotheight), width = 3)

        self.numbers = []
        
        one = random.randint(0, 9)
        two = random.randint(0, 9)
        three = random.randint(0, 9)
        
        self.numbers.append((self.slot.create_text((self.slotwidth/6 + 5, self.slotheight/2), text = one, font = "helvetica 35"), one, 1))
        self.numbers.append((self.slot.create_text((3*self.slotwidth/6 + 5, self.slotheight/2), text = two, font = "helvetica 35"), two, 2))
        self.numbers.append((self.slot.create_text((5*self.slotwidth/6 + 5, self.slotheight/2), text = three, font = "helvetica 35"), three, 3))

        for i in [-4,-3,-2,-1,1,2,3,4,5]:
            self.numbers.append((self.slot.create_text((self.slotwidth/6 + 5, 13*i*self.slotheight/30 + self.slotheight/2), text = (one+i) % 10, font = "helvetica 35"), one, 1))
            self.numbers.append((self.slot.create_text((3*self.slotwidth/6 + 5, 13*i*self.slotheight/30 + self.slotheight/2), text = (two+i) % 10, font = "helvetica 35"), two, 2))
            self.numbers.append((self.slot.create_text((5*self.slotwidth/6 + 5, 13*i*self.slotheight/30 + self.slotheight/2), text = (three+i) % 10, font = "helvetica 35"), three, 3))

        self.question = "Je {} menší nebo větší než {}?"
        self.text = Text(self, font = "helvetica 20", relief = "flat", background = "white",
                         width = 80, height = 2, pady = 7, wrap = "word")
        self.text.grid(row = 3, column = 1, columnspan = 2)
        self.text.tag_configure("center", justify = "center")

        ttk.Style().configure("TButton", font = "helvetica 18")
        
        self.lower = ttk.Button(self, text = "Menší", command = self.lowerResponse)
        self.lower.grid(row = 5, column = 1)

        self.higher = ttk.Button(self, text = "Větší", command = self.higherResponse)
        self.higher.grid(row = 5, column = 2)

        self.columnconfigure(0, weight = 4)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 4)
        
        self.rowconfigure(0, weight = 7)
        self.rowconfigure(1, weight = 4)
        self.rowconfigure(3, weight = 2)
        self.rowconfigure(4, weight = 3)
        self.rowconfigure(6, weight = 6)

        self.number = 0
        self.displayQuestion()
        self.t0 = perf_counter()


    def randomize(self):
        self.random["state"] = "disabled"
        self.starttime = perf_counter()
        self.time0 = self.starttime
        self.time = self.time0
        self.endtime = self.time + random.randint(7, 15)
        while self.time < self.endtime:
            self.time = perf_counter()
            for obj in self.numbers:
                x, y = self.slot.coords(obj[0])
                if y > 1.1*self.slotheight:
                    y -= self.slotheight*13*10/30
                y += (self.time - self.time0) * 1000
                self.slot.coords(obj[0], x, y)
            self.time0 = self.time
            self.update()
        

    def lowerResponse(self):
        self.response("lower")

    def higherResponse(self):
        self.response("higher")        

    def displayQuestion(self):
        self.anchor = random.randint(1, 1000)
        self.text["state"] = "normal"
        self.text.delete("1.0", "end")
        self.text.insert("end", self.question.format(items[self.number][1], self.anchor), "center")
        self.text["state"] = "disabled"


    def response(self, answer):
        self.file.write("\t".join([self.id, items[self.number][0], str(self.anchor), answer,
                                   str(perf_counter() - self.t0)]) + "\n")
        self.number += 1
        self.proceed()

    def proceed(self):
        if self.number == len(items):
            self.nextFun()
        else:
            self.displayQuestion()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Comparison])
