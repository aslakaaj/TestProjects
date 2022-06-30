from tkinter import *
import random

root = Tk()

root.geometry('400x250')

lblTitle = Label(root, text = "Are you an idiot?", font = ("Courier", 20))
lblTitle.place(x=50, y=50)

btnYes = Button(root, text = 'Yes')
btnYes.place(x = 50, y = 200)

btnNo = Button(root, text = 'No')
btnNo.place(x = 100, y = 200)

def NewBtnPosition(event):
	x = random.randint(60,350)
	y = random.randint(70,200)
	btnNo.place(x = x, y = y)

def PressedYes(event):
    btnNo.destroy()
    btnYes.destroy()
    lblTitle.config(text="Okey then!")
	
btnNo.bind("<Button-1>", NewBtnPosition)
btnYes.bind("<Button-1>", PressedYes)

root.mainloop()
