#-------------------------------------------------------------
#프로그램 기능 구현상 예외 발생시키기
#raise 예외객체
#-----------------------------------------------------------------

num = int(input("3의 배수 입력 : "))
try:                                                    #try exception 오류 발생시만
    if num %3 != 0:
        print(f'{num}은 3의 배수가 아닙니다.')
        raise  Exception("3의 배수 오류")
except Exception as ex:
    print("에러 발생")

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print(("Dfdfdf"))

e=Eagle()
e.fly()