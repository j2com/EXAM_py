#ent.config(show='*') >> 입력 문자 숨기기
#ent.insert(0, 'temp@temp.com) 입력창 문자열 삽입 0 =1번쨰 자리 삽입하려는 내용
#ent.delete(0,3) 입력창 문자열 삭제 0~2번째 문자열 삭제
#ent.bind("<Button-1>",clear) 입력창 클릭시 명령 Button-1 >> 좌클릭 다음 실행할 함수

from tkinter import *

win = Tk()
win.title('Daum Log-in')
win.geometry('400x300')
win.option_add('*Font','궁서 20')
#다음 로고
lab_d = Label(win)
img = PhotoImage(file='C:\Users\ss\Pictures\Saved Pictures', master = win)
lab_d.config(image=img)
lab_d.pack()
#id 라벨
lab1 = Label(win)
lab1.config(text='ID')
lab1.pack()
#id 입력창
ent1 = Entry(win)
ent1.pack()
#pw 라벨
lab1 = Label(win)
lab1.config(text='Password')
lab1.pack()
#pw 입력창
ent2 = Entry(win)
ent2.pack()

#로그인 버튼
btn = Button(win)
btn.config(text='로그인')
btn.pack()



win = mainloop()