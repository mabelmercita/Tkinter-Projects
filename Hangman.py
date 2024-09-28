from tkinter import * 
import random

root=Tk()
root.title("Hangman")
root.geometry("600x400")

wordList=['GIRL','BUTTER','DOG','SCIENCE','XEROX']
random.shuffle(wordList)

n=0
tries=6
word=''
dashes=[]
misses=[]

def newround():
    global wordlist,word,n,tries
    word=wordList[n]
    dashes.clear()
    for i in range(len(word)):
        dashes.append('_')
    wl.config(text=dashes)
    misses.clear()
    ll.config(text='')
    tries=6
    gl.config(text='tries left:6')

def check():
    global dashes,tries,word,n
    intercal;get()
gl=Label(root,text="tries left : 6")
gl.pack()

ll=Label(root,text="")
ll.pack()

wl=Label(root,text="_ _ _")
wl.pack()

e1=Entry(root)
rl=Label(root,text="")
rl.pack()

newround()
mainloop()