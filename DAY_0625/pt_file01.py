import os

DIR_PATH = './AddressBook/'

def printMenu():
    print("="*7+'ADDRESSBOOK'+'='*7)
    print(" "*7+'1. 전체보기')
    print(" "*7+'2. 검   색')
    print(" "*7+'3. 추   가')
    print(" "*7+'4. 종   료')
    print('=' * 26)
def initApp():
    if not os.path.exists(DIR_PATH): os.mkdir(DIR_PATH)
    dataList = os.listdir(DIR_PATH)
def showAdd():
    dataList = os.listdir(DIR_PATH)
    for info in dataList:
        print(f'{info[:8]}')

def addAdd(name, phone, loc, email):
    with open(DIR_PATH+name+"_"+phone[3:7]+".txt",mode='w',encoding='utf-8') as f:
        f.write(name+" "+phone+" "+loc+" "+email)

def searchAdd(name_phone):
    dataList = os.listdir(DIR_PATH)
    for add in dataList:
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH+add, mode='r', encoding='utf-8') as f:
                print(f'정  보 : {f.read()}')


initApp()
while True:

    printMenu()
    sel = input("메뉴 선택 : ")
    if sel in '4': break

    elif sel in '1':
        showAdd()
    elif sel in '2':
        search = input()
        searchAdd(search)
    elif sel in '3':
        name, phone, loc, email = input().split()
        addAdd(name, phone, loc, email)



