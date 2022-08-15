import os
DIR_PATH = '../AccountBook/'
dateList = os.listdir(DIR_PATH)
def print_f():
    print("=" * 7 + '가 계 부' + '=' * 7)
    print(" " * 7 +'1. 일자별 지출 금액')
    print(" " * 7 +'2. 카테고리별 지출 금액')
    print(" " * 7 +'3. 모든 데이터')
    print(" " * 7 +'4. 총 지출 금액')
    print(" " * 7 +'5. 데이터 추가')
    print('=' * 26)


def dateShow(partDate): #날짜별 내역 보여주기
    dateList = os.listdir(DIR_PATH)
    for date in dateList:
        if partDate == date[:4]:
            with open(DIR_PATH+partDate+".txt", mode= 'r', encoding= 'utf-8') as f:
                print(f.read())

def dateAllshow():        #모든 내역 보여주기
    dateList = os.listdir(DIR_PATH)
    for date in dateList:
        with open(DIR_PATH + date , mode='r', encoding='utf-8') as f:
            print(f.read())

def dateSum(): # 일별 총 합계

    for date in dateList:
        with open(DIR_PATH + date, mode='r', encoding='utf-8') as f:
            dateSum = 0

            for i in range(0,3): #교통비 식비 쇼핑 3줄 읽기라 3번 반복

                paySum = f.readline()
                dateSum += int(paySum[4:])
            print(dateSum)

def partPay(payName): # 일별 카테고리별 합계

    transpaySum = 0
    eatpaySum = 0
    shoppaySum = 0
    for date in dateList:

        with open(DIR_PATH + date, mode='r', encoding='utf-8') as f:

            for i in range(0,3):
                transpay = 0
                eatpay = 0
                shoppay = 0
                partPay = f.readline()
                if partPay[:3] == "교통비":
                    transpay += int(partPay[4:])
                elif partPay[:3] == "식사비":
                    eatpay += int(partPay[4:])
                elif partPay[:3] == "쇼핑비":
                    shoppay += int(partPay[4:])
                transpaySum += transpay
                eatpaySum += eatpay
                shoppaySum += shoppay
    if payName == '교통비':
        print(f'일별 교통비 합계 : {transpaySum}')
    if payName == '식사비':
        print(f'일별 식사비 합계 : {eatpaySum}')
    if payName == '쇼핑비':
        print(f'일별 쇼핑비 합계 : {shoppaySum}')

def allSum(): # 일별 카테고리별 합계

    transpaySum = 0
    eatpaySum = 0
    shoppaySum = 0
    for date in dateList:

        with open(DIR_PATH + date, mode='r', encoding='utf-8') as f:

            for i in range(0,3):
                transpay = 0
                eatpay = 0
                shoppay = 0
                partPay = f.readline()
                if partPay[:3] == "교통비":
                    transpay += int(partPay[4:])
                elif partPay[:3] == "식사비":
                    eatpay += int(partPay[4:])
                elif partPay[:3] == "쇼핑비":
                    shoppay += int(partPay[4:])
                transpaySum += transpay
                eatpaySum += eatpay
                shoppaySum += shoppay
    allSum = transpaySum + eatpaySum + shoppaySum
    print(allSum)

def dateAdd(date, name, pay):
    with open(DIR_PATH+date+".txt",mode='a',encoding='utf-8') as f:
        f.write(name+" "+pay+"\n")

print_f()
dateInput = input()
while True:
    if dateInput == '1':
        partDate = input("날짜를 입력하세요 : ")
        dateShow(partDate)

    elif dateInput == '2':
        payName = input("카테고리 입력하세요 : ")
        partPay(payName)
    elif dateInput == '3':
        dateAllshow()
        break
    elif dateInput == '4':
        allSum()
    elif dateInput == '5':
        for i in range(0,3):
            date, name, pay = input("날짜, 이름, 금액을 입력하세요 : ").split()
            dateAdd(date, name, pay)
        break

