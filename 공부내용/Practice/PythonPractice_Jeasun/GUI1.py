from tkinter import*#모듈에 있는 함수를 포함
window = Tk()#버튼 위젯을 생성

button = Button(window,text ="클릭!")#윈도우객체,텍스트
button.pack()#버튼을 최대한 압축하여 윈도우에 표시

window.mainloop()#윈도우 에서 발생하는 여러가지 이벤트를 처리하는 함수