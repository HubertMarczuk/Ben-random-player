from playsound import playsound
from random import random
from tkinter import *
from math import floor
from PIL import ImageTk, Image


class Ben(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry("576x700")
        self.window.title("Ben")
        self.BuildWindow()
        playsound("./sounds/phone.wav")
        self.window.mainloop()

    def BuildWindow(self):
        self.DisplayGif("./images/phone.png")

        self.button = Button(self.window, width=16)
        self.button["text"] = "Ask Ben"
        self.button["command"] = self.Ask
        self.button.grid(row=1, column=0)

    def Ask(self):
        seed = random()
        seed = int(floor(seed * 6))
        if seed == 0 or seed == 1:
            self.DisplayGif("./images/yes.png")
            playsound("./sounds/yes.wav")
        elif seed == 2:
            self.DisplayGif("./images/hoho.png")
            playsound("./sounds/hoho.wav")
        elif seed == 3:
            self.DisplayGif("./images/ugh.png")
            playsound("./sounds/ugh.wav")
        else:
            self.DisplayGif("./images/no.png")
            playsound("./sounds/no.wav")

    def DisplayGif(self, path):
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        self.label = Label(self.window, image=photo)
        self.label.grid(row=0, column=0)
        self.label.image = photo


ben = Ben()
