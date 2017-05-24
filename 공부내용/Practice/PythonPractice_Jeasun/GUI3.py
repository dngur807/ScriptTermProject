from tkinter import*
window = Tk()
#라벨을 만든다
l1 = Label(window,text="달러")
l2 = Label(window,text="원")
l1.pack()
l2.pack()

#공백을 넣는다
e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

#버튼을 만든다.
b1 = Button(window,text="달러->원")
b2 = Button(window,text="원->달러")
b1.pack()
b2.pack()

window.mainloop()