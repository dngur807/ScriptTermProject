from tkinter import*
# 최상위 윈도우를 생성(윈도우 창)
window = Tk()

#라벨#격자 배치
l1 = Label(window,text = "달러")
l2 = Label(window,text = "원")
l1.grid(row=0,column = 0)
l2.grid(row=1,column=0)

#입력 빈칸
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0,column=1)
e2.grid(row=1,column=1)

#버튼
b1 = Button(window,text = "달러->원")
b2 = Button(window,text = "원->달러")
b1.grid(row = 2, column = 0)
b2.grid(row=2,column = 1)

window.mainloop()
