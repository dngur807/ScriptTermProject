from tkinter import*
window = Tk()
def process():
    dollar = float(e1.get())
    e2.insert(0,str(dollar*1200))

def process2():
    dollar = float(e2.get())
    e1.insert(0,str(dollar/1200))

l1 = Label(window,text = "달러")
l2 = Label(window,text = "원")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0,column = 1)
e2.grid(row=1,column = 1)

b1 = Button(window,text="달러->원",command=process)
b2 = Button(window,text="원->달러",command=process2)
b1.grid(row = 2,column = 0)
b2.grid(row=2,column = 1)

window.mainloop()