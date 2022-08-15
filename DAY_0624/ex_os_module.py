#-----------------------------------------------------------------------------
# File & Dir 관련 모듈
#_---------------------------------------------------------------------
import os
import os.path as path

#특정 폴더 존재 여부 + > 없으면 폴더 생성하기

DIR_PATH = './Image/jpg/02/000'
if not path.exists(DIR_PATH):
#   os.mkdir(DIR_PATH)               #1개 폴더 생성
    os.makedirs(DIR_PATH)         #하위 폴더까지 생성
DATA_FILE=DIR_PATH+'/flower.jpg';
if not path.exists(DATA_FILE):
    print('파일 없음')

#특정 경로 안에 존재하는 내용 리스트 화 ----------------------------------------------------
dataList = os.listdir('./Addressbook')
print(dataList)

#시간 관련 모듈 ------------------------
import  time as t

#현재 시간
print(t.time())
print(t.localtime(t.time()))

curTime = t.localtime(t.time())
print(curTime.tm_year, curTime.tm_hour, curTime.tm_wday)

# 2022-06-24 2022/06/24 24/06/2022 localtime 쓰기 위해 문자열로

for num in range(10):
    t.sleep(0.5)
    print('[num]', end='')  # ex)) 로딩에 활용

#과제 2 : 과제1에 기능 업데이트
#1.프로그램 초기화 기능 함수
# 프로그램 끝나고 돌어왔을때 Addressbook 폴더 내의 파일리스트 정보 가져오기
#2 파일 & 폴더 관련 모듈 활용
#    -변경하고자 하는 부분 변경하기! 파일에 access 리스트가 필요한지 없는지 (지워라) os 함수 활용
# 파일명 저장 리스트 존재 여부 선택
#처음 실행했을떄 폴더 없으니 init에서 폴더를 만들어라
