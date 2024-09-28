from tkinter import*
import random
root=Tk()
root.title('Word Unscrambler')
root.geometry('600x400')

wordlist=['SPRING','TEACHER','COST','ANIMAL','KITE','ORANGE']
random.shuffle(wordlist)
score=0
time=0
word=''
n=0
completed=False

def cu():
    global time
    if not completed:
        time+=1
        tm1.config(text='Time:'+str(time))
        root.after(1000,cu)

def jumble():
    global word
    word=wordlist[n]
    jumble=random.sample(word,len(word))
    w1.config(text=jumble)

def check(event):
    global word,score,n,completed
    if e.get().upper()==word and not completed:
      score+=1
      s1.config(text='Score:'+str(score))
      e.delete(0,END)
      n+=1
      if n<len(wordlist):
          jumble()
      else:
         completed=True
         r1.config(text='You complted in'+str(time)+'seconds') 
                   
t1=Label(root,text='Unscramble all the words in the shortest possible time',font=('Arial Bold',15))
t1.grid(row=0,column=0)

s1=Label(root,text='Score=0')
s1.grid(row=1,column=0,sticky=W)

tm1=Label(root,text='Time=0')
tm1.grid(row=1,column=1,sticky=E)

w1=Label(root,text='',font=('Arial',60))
w1.grid(row=2,column=0,columnspan=2)

e=Entry(root)
e.grid(row=3,column=0,columnspan=2)

r1=Label(root)
r1.grid(row=4,column=0,columnspan=2)

root.after(1000,cu)
jumble()
root.bind('<Return>',check)
mainloop()