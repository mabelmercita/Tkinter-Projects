from tkinter import*
root=Tk()
root.title('Addition Calculator')
root.geometry('350x200')

def add():
    if e1.get().isnumeric() and e2.get().isnumeric():
        n1=int(e1.get())
        n2=int(e2.get())
        sum=n1+n2
        s1.config(text=sum)
    else:
        s1.config(text='Please enter a number')
e1=Entry(root)
e1.pack()

a1=Label(root,text='+',font=('Arial',35))
a1.pack()

e2=Entry(root)
e2.pack()

b1=Button(root,text='=',command=add)
b1.pack()

s1=Label(root)
s1.pack()

mainloop()