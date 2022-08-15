#----------------------------------------------------------------------
#파일 읽고 쓰기 input stream output stream
#--------------------------------------------------------------

filename = 'mydate.txt'  #경로 66지정

#파일 쓰기
#(1) 파일 열기
#mode ='w' >> 파일 없으면 생성 후 쓰기
#          >> 파일 있으면 내용 지우고 쓰기
file = open(filename, mode='a', encoding='utf-8')

#mode 'a' >> 파일 없으면 생성 후 쓰기 (a는 append)
#         >> 파일 있으면 덧붙이기

#(2) 파일 쓰기
file.write('Good\n')      #\n줄바꿈
file.write('Happy\n') #str tpye만 가능 숫자도 문자임 ' ' 안에 입력 무조건!! 읽고 쓰기 할떄


#(3) 파일 닫기
file.close()

#(파일 읽기)
#(1)파일 열기
file = open(filename, mode='r')

#(2)파일 읽기
data=file.read(6)   #공백 포함 6개
print(f'read data => {data}')
print(f'read data type - => {type(data)}')
                        #읽고 나면 커서 제일 끝으로 이동함 so data2 read 시 0 출력
file.seek(0)          #0번 자리로 가라! 커서 제일 앞으로 감
data2 = file.read()
print(f'read data2 => {data2}, len = {len(data2)}')

file.seek(0)
#파일에서 1줄 읽기
data3=file.readline()   #readlines = 줄들을 가져와 리스트에 담아서 줌
print(f'read data3 => {data3}')

#1줄씩 읽어서 리스트에 담아서 가져오기
data4 = file.readlines()
print(f'read data4 => {data4}')

#


#(3)파일 닫기
file.close()