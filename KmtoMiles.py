from tkinter import*
root=Tk()
root.geometry('300x400')
l1=Label(root,text='Convert Km to miles',font=('Arial',10))
l1.grid(row=0,column=0,columnspan=2)

def cn():
    km=int(e1.get())
    m=km*0.621
    r1.config(text=m)

l1=Label(root,text='Kilometer:')
l1.grid(row=1,column=0)

l2=Label(root,text='Miles:')
l2.grid(row=2,column=0)

e1=Entry(root)
e1.grid(row=1,column=1)


r1=Label(root)
r1.grid(row=2,column=1)

b1=Button(root,text='Convert',command=cn)
b1.grid(row=3,column=0,columnspan=2)

mainloop()