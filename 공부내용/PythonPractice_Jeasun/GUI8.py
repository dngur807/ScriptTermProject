from tkinter import*
window = Tk()

l1 = Label(window,text="김영식",bg = "red",fg="white",font='helvetica 16 italic')
l2 = Label(window,text="이재영",bg = "green",fg="white")
l3 =  Label(window,text="이제선",bg = "blue",fg="white")
l1.place(x=0,y=0)
l2.place(x=100,y=30)
l3.place(x=150,y=60)



window.mainloop()