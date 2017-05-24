from tkinter import*

def process():
    print("한국산업기술대학교")

window = Tk()
button =  Button(window,text="클릭!", command=process)
button.pack()
window.mainloop()