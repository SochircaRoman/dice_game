from tkinter import *
import random

class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x200')
        self.title('My game using Python!')
        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file=('icon.png')))
        self.bg = PhotoImage(file=('background.png'))

        self.setUi()




    def setUi(self):
        Label(self, image=self.bg).pack()

        self.lab_left = Label()
        self.lab_left.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.lab_right = Label()
        self.lab_right.place(relx=0.7, rely=0.5, anchor=CENTER)

        self.btn1 = Button(self, text='THROW',fg='white', bg='black', command=lambda : self.change())
        self.btn1.place(relx=0.5, rely=0.1, anchor=CENTER)

    def start(self):
        x = random.choice(['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png', 'im6.png'])
        return x

    def change(self):
        self.ex1 = PhotoImage(file=(self.start()))
        self.ex2 = PhotoImage(file=(self.start()))
        self.lab_left['image'] = self.ex1
        self.lab_right['image'] = self.ex2



root = Game()
root.mainloop()