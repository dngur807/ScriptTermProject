# -*- coding: euc-kr -*-
from tkinter import*
def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image = img)
    imageLabel.image = img

window = Tk()
photo = PhotoImage(file = 'dd.gif') #����Ʈ �̹��� ����

#�󺧿� �̹����� ����
imageLabel = Label(window, image=photo)
imageLabel.pack()

#��ĭ
inputBox = Entry(window)
inputBox.pack()

#��ư
button = Button(window, text='Ŭ��', command=change_img)
button.pack()

window.mainloop()


