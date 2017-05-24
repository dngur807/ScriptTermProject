# -*- coding: euc-kr -*-
from tkinter import*
def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image = img)
    imageLabel.image = img

window = Tk()
photo = PhotoImage(file = 'dd.gif') #디폴트 이미지 파일

#라벨에 이미지를 넣음
imageLabel = Label(window, image=photo)
imageLabel.pack()

#빈칸
inputBox = Entry(window)
inputBox.pack()

#버튼
button = Button(window, text='클릭', command=change_img)
button.pack()

window.mainloop()


