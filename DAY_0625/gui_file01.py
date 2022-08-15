from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk() #창 생성

win.geometry('300x100')
win.option_add('*Font',"궁서 15")

ent = Entry(win) # win창에 입력창을 만들어라
ent.pack()
def lotto_p():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')
    soup_f = soup.find('div', attrs={'class','win_result'}).getText()
    soup_f1 = soup_f.split('\n')
    num_list = soup_f1[7:13]
    bonus = soup_f1[-4]
    print(f'당첨번호 : {num_list}')
    print(f'보너스 : {bonus}')


btn = Button(win)
btn.config(text = '로또 당첨 번호 확인')
btn.config(command=lotto_p)
btn.pack()

win.mainloop()