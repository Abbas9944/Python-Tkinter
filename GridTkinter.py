from tkinter import *
import datetime
root = Tk()
root.geometry('300x400')

time = datetime.datetime.now().strftime("%H:%M:%S")
day = datetime.datetime.now().day
f3 = Frame(root,bg='red',borderwidth=5,relief=SOLID)
l3 = Label(f3,text="Label 1",padx=15,pady=15).pack(pady=10)
btn1 = Button(text="Button",borderwidth=5,relief=SOLID).pack()
f3.pack(side=RIGHT,fill=Y)

f1 = Frame(root,bg='red',borderwidth=5,relief=SOLID)
l1 = Label(f1,text="Label 1",padx=15,pady=15).pack(pady=150)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root,bg='red',borderwidth=5,relief=SOLID)
l2 = Label(f2,text=time,padx=15,pady=15).pack(padx=150)
f2.pack(side=TOP,fill=X)

f4 = Frame(root,bg='red',borderwidth=5,relief=SOLID)
l4 = Label(f4,text=day,padx=15,pady=15).pack(padx=150)
f4.pack(side=BOTTOM,fill=X)


root.mainloop()