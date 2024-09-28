from tkinter import*
root=Tk()
root.geometry('500x400')

list=[]

def add():
    global list
    list.append(e1.get())
    lb.insert('end',e1.get())
    e1.delete(0,END)
    savelist()

def clear():
    global list
    list.clear()
    lb.delete(0,END)
    savelist()

def delete():
    global list
    item=lb.get('active')
    list.remove(item)
    for i in lb.curselection():
        lb.delete(i)
    savelist()

def savelist():
    f=open(r'C:\Users\MabelManuel\OneDrive\Desktop\TO DO.txt','w')
    for i in list:
        f.write(i)
        f.write('\n')
    f.close()

def retrieve():
    global list
    f=open(r'C:\Users\MabelManuel\OneDrive\Desktop\TO DO.txt','r')
    s=f.read()
    f.close()
    l=s.split('\n')
    for i in l:
        lb.insert(END,i)

frame=Frame(root)
frame.pack()

e1=Entry(frame)
e1.grid(row=0,column=0,columnspan=3)

ab=Button(frame,text='ADD',command=add)
ab.grid(row=1,column=0)

db=Button(frame,text='DELETE',command=delete)
db.grid(row=1,column=1)

cb=Button(frame,text='CLEAR',command=clear)
cb.grid(row=1,column=2)

lb=Listbox(frame)
lb.grid(row=2,column=0,columnspan=3)

retrieve()
mainloop()