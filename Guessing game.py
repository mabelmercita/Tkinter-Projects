from tkinter import *
import random

root=Tk()
root.title("Guessing game")
root.geometry("400x200")

tries=7
number=random.randint(1,100)

def check():
    global tries
    if tries >0:
        guess=int(e1.get())
        tries-=1
        l2.config(text='Tries:'+str(tries))
        if n

l1=Label(root,text="Guess a number between 1 and 100",font=("Arial",17))
l1.pack()

e1=Entry(root)
e1.pack()

l2=Label(root,text = 'Tries:7')
l2.pack()

l3=Label(root,text = '')
l3.pack()

mainloop()
