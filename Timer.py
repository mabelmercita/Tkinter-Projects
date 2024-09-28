from tkinter import*
root=Tk()
time=60
def countdown():
    global time
    time-=1
    t1.config(text='Time:'+str(time))
    if time>0:
        root.after(1000,countdown)     
t1=Label(root,text='Time:60')
t1.pack()

root.after(1000,countdown)
mainloop()