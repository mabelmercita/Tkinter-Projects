from tkinter import*
root=Tk()

def bc():
   if e1.get().isnumeric():
      number=int(e1.get())
      if number%2==0:
         r1.config(text='Even Number')
      else:
         r1.config(text='Odd Number')
   else:
      r1.config(text='Please enter a number')

t1=Label(root,text='ODD/EVEN',font=('Comic MS Sans',40))
t1.pack()

i1=Label(root,text='Enter a number',fg='Purple')
i1.pack()

e1=Entry(root,bg='blue')
e1.pack()

b1=Button(root,text='CHECK',command=bc)
b1.pack()

r1=Label(root)
r1.pack()

mainloop()