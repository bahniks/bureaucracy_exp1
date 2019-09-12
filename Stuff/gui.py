from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import localtime, strftime

import os


class GUI(Tk):
    def __init__(self, frames):
        super().__init__()
        
        self.title("Experiment")
        self.state("zoomed")
        self.config(bg = "white")
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.protocol("WM_DELETE_WINDOW", lambda: self.closeFun())
        #self.geometry("1366x768") # for testing

        self.screenwidth = 1366 # adjust
        self.screenheight = 768 # adjust

        filepath = os.path.join(os.getcwd(), "Data")
        if not os.path.exists(filepath):
            message = "Zavolejte prosím experimentátora."
            secondary = "Složka pro ukládání výsledků neexistuje.\nJe potřeba vytvořit "\
                        "složku Data ve stejné složce, kde je umístěn soubor s experimentem."            
            messagebox.showinfo(message = message, icon = "error", title = "Chyba",
                                parent = self, detail = secondary)
            self.destroy()
            return
        
        writeTime = localtime()
        self.outputfile = os.path.join(filepath, strftime("%y_%m_%d_%H%M%S", writeTime) + ".txt")

        self.bind("<Escape>", self.closeFun)

        self.order = frames
                                    
        self.count = -1

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
                      
        with open(self.outputfile, mode = "w") as self.file:
            self.nextFrame()
            self.mainloop()
        

    def nextFrame(self):
        self.count += 1
        if self.count >= len(self.order):
            self.destroy()
        else:
            nxt = self.order[self.count]
            if isinstance(nxt, tuple):
                self.frame = nxt[0](self, **nxt[1])
            else:
                self.frame = nxt(self)
            self.frame.grid(row = 0, column = 0, sticky = (N, S, E, W))

            if hasattr(self.frame, "run"):
                self.update()
                self.frame.run()


    def closeFun(self, event = ""):
        message = "Jste si jistí, že chcete studii předčasně ukončit? "
        ans = messagebox.askyesno(message = message, icon = "question", parent = self,
                                  title = "Ukončit studii?")
        if ans:
            self.destroy() 
