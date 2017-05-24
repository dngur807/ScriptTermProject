from tkinter import*
window = Tk()

def process():
    e2.insert(0,"환율 : 1달러 = 1200원")#e2빈칸 에 넣어준다,

l1 = Label(window,text = "달러")
l2 = Label(window,text = "원")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0,column = 1)
e2.grid(row=1,column = 1)

b1 = Button(window,text="달러->원",command=process)
b2 = Button(window,text="원->달러")
b1.grid(row = 2,column = 0)
b2.grid(row=2,column = 1)

window.mainloop()