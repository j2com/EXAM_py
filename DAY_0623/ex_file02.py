#----------------------------------------------------
#path => 경로
#   절대경로 : 파일 및 폴더 존재하는 위치의 경로
#   상대경로 : 현재 코드 파일 기준으로 경로를 지정 ex)지금 파일 기준
#   .: 현재 위치
#   ..: 상위 한단계 위
#   현재위치 : f.tell


filename ='../Data/home.html'
filename = './html/home.html'


# home.html 파일을 라인 단위로 읽어서 화면에 출력하기

file = open(filename, mode= 'r', encoding='utf-8')
#data = file.read()
#print(f'{data}')
while True:
     data = file.readline()
     if not data : break
     data = data.strip()
     if len(data) > 0 : print(data)

file.close()

# with 파일 as 구문 close가 필요 없다!!

with open(filename, mode = 'r', encoding= 'utf-8') as file:
    while True:
        data = file.readline()
        if not data: break
        data = data.strip()
        if len(data) > 0 : print(data)