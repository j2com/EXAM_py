#객체 들어가는 곳 - 힙 변수 들어가는 곳 - 스택
# 모듈(Module) : 하나의 파이썬(.py) 파일
#               특정 목적에 관련된 변수, 함수, 클래스 존재
#               필요한 파일에서 사용 가능 함
# 사용법 : import 모듈명
#------------------------------------------------------------------------------------------------------------
#종이모양 : 모듈  폴더모양 : 패키지

#모듈 포함하기
#import math
from math import factorial
#모듈 안에 기능 사용하기-------------------------------------------------------------
print(factorial(5))
import ex_func

print(ex_func.YEAR, ex_func.printYear())


#--------------------------------------------------------------
#PROGRAM : Addressbook.APP
#DESCRIPTION : file I/O 처리, str 데이터 처리, Function 실습
#(1) Addressbook 폴더에 개인 파일 생성 --> 이름_전화번호.txt
#(2)보기, 검색, 추가, 종료 기능 => 메뉴 출력
#(3)종료 입력 전까지 무한 반복
#--------------------------------------------------------------
#전역변수 및 상수 선언------------------------------- 폴더명 고정
DIR_PATH = '../Addressbook' # 파일 저장 폴더
ADDR_LIST = ['가_111', '가나다_111']              # 주소 파일 저장 리스트


#함수 정의 --------------------------------------
#메뉴 출력 함수-------------------------------
#함수명 : printmenu
#파라미터 :x
#리턴값 :x
#-------------------------------------------
def printmenu():
    print('='*7 + 'ADDRESSBOOK' + '=' * 7)
    print('='*7 + "1. 전체보기")
    print('='*7 +"2. 검   색")
    print('='*7 +"3. 추   가")
    print('='*7 +"4. 종   료")
    print('=' *26)

#전체 전화번호 리스트 출력 함수--------------------------
#함수명 : showAddress
#파라미터 :x
#리턴값 : x
#-------------------------------------------
def showAddress():
    print('현재 등록된 주수록 정보')
    for addr in ADDR_LIST:
        print(addr)

#--------------------------------------------
#등록된 주소 검색 후 정보 출력 함수-----------------
#함수명 : searchAddress
#파라미터 : name or phone_number str data
#리턴값 : 없음
#----------------------------------------------

#------------------------------------
#프로그램 초기화 함수----------------
# ADDR_LIST 에 Address안에 존재하는 파일 리스트 정보가 추가
#함수명 : initapp
#파리미터 : x
#반환값 : x
def initApp():
    pass






def searchAddress(name_phone):
# 파일명 리스트 안에서 해당 검색어 존재 여부 체크
    for add in ADDR_LIST:
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH+add+'.txt', mode = 'r', encoding= 'utf-8') as f: #파일 생성할 위치 + 이름
                print(f'정 보 : {f.read()}')

#주소록 파일 생성 및 추가 함수----------------------------------
#함수명 : addAddress
#파리미터 : 이름, 전화번호, 지역, 이메일
#반환값 : x
#------------------------------------------------

def addAddress(name, phone, loc, email):
    filename = name+'_'+phone+'.txt'
    #파일명 리스트 추가
    ADDR_LIST.append(filename[:-4])
    #Addressbook 폴더에 파일 생성
    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + loc + ' ' + email)
#기능 구현 ---------------------------------------

print('--------프로그램 시작합니다.!!')
while True:
    printmenu()
    #사용자로부터 메뉴 선택 받기
    select = input("메뉴 선택 : ")
    if select == '4':break

    elif select == '1':
        showAddress()

    elif select == '2':
        search = input("이름 또는 전화번호")
        searchAddress(search)

    elif select == '3':
        search = input("이름, 전화번호, 지역, 이메일 : (예 : 홍길동, xxx-xxxx-xxxx,대구,aaa@sdf").split(",")

        searchAddress(search[0],search[1],search[2],search[3])
    else:
        print('해당 메뉴는 존재하지 않습니다.')




print('--------프로그램 종료합니다.')