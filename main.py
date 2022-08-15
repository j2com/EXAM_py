from tkinter import *
from datetime import datetime


win = Tk() #창 생성

win.geometry('600x500')
win.title('What time?')
win.option_add('*Font',"궁서 15")
def what_time():
    dnow = datetime.now()
    btn.config(text= dnow)


btn = Button(win) # 버튼 생성 () >> 어떠한 창 안에 넣을 것이냐
btn.config(width= 30, height=2) #버튼 크기
btn.config(text= "현재 시각") #버튼 내용
btn.config(command=what_time) #버튼 기능
btn.pack() #버튼 배치

ent = Entry(win) # win창에 입력창을 만들어라
ent.get() #입려강 / 내용 추출
ent.pack()

win.mainloop() #창 실행