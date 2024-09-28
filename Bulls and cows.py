from tkinter import*
import random

root=Tk()
root.geometry('600x600')
root.title('BULLS AND COWS')

tries=15
number=str(random.randint(1000,9999))

while len(set(number))!=4:
    number=str(random.randint(1000,9999))

def check(event):
    guess=e1.get()
    if guess.isnumeric() and len(guess)==4 and len(set(guess))==4:
        global tries
        tries-=1
        bulls=0
        cows=0
        label2.config(text='tries: '+str(tries))
        label3.config(text='')
        e1.delete(0,END)
        for i in range(4):
            if guess[i]==number[i]:
                bulls+=1
            elif guess[i] in number:
                cows+=1
        l4=Label(root,text=f'{guess} bulls-{bulls} cows-{cows}')
        l4.pack()

        if bulls==4:
            label3.config(text='you found the secret number')
        elif tries==0:
            label3.config(text='Sorry! No tries left! The secret number is '+number)
    
    else:
        label3.config(text='Error')

label1=Label(root,text='Guess the 4- digit secret number with unique digits',font=('Arial',18))
label1.pack(pady=10)

label2=Label(root,text='Tries:15')
label2.pack(pady=10)

e1=Entry(root)
e1.pack(pady=10)

label3=Label(root)
label3.pack(pady=10)

root.bind('<Return>',check)
mainloop()