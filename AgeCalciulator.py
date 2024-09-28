from tkinter import*
root=Tk()
root.title('Age Calculator')
root.geometry('350x200')

def Calc():
    if e1.get().isnumeric():
        y=int(e1.get())
        age=2023-y
        r1.config(text=age)
    else:
        r1.config(text='Please enter a number')
        
t1=Label(root,text='Enter your Year of Birth',font=('Arial',15))
t1.pack()

e1=Entry(root)
e1.pack()

b1=Button(root,text='SUBMIT',command=Calc)
b1.pack()

r1=Label(root)
r1.pack()

mainloop()