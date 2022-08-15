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
