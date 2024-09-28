from tkinter import*
root=Tk()
root.geometry('300x200')

def encode():
    word=e1.get()
    answer=''
    for i in word:
            if i=='z':
                answer+='a'
            elif i =='Z':
                answer+='A'
            else:
                unicode=ord(i)
                unicode+=1
                letter=chr(unicode)
                answer+=letter
    l1.config(text=answer)

def decode():
    word=e1.get()
    answer=''
    for i in word:
            if i=='a':
                answer+='z'
            elif i =='A':
                answer+='Z'
            else:
                unicode=ord(i)
                unicode-=1
                letter=chr(unicode)
                answer+=letter
    l1.config(text=answer)

e1=Entry(root)
e1.pack()

b1=Button(root,text='ENCODE',command=encode)
b1.pack()

b2=Button(root,text='DECODE',command=decode)
b2.pack()

l1=Label(root,text='')
l1.pack()

mainloop()