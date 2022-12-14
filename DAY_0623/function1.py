#---------------------------------------------------------------------------------------
#함수(Function) : 자주 사용되는 기능을 묶어서 이름을 붙여 놓은 것
#   코드 재사용 위한 것
#형태
#def 함수명(재료, ......):
#   코드
#   코드
#   return 결과
#-----------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
# 기        능 : 숫자 2개 더한 후 결과 돌려주는 기능
# 함수명        : addTwo
# 재료(매개변수) : num1, num2
# 결과(반환값) : 더한 값

def addTwo(num1, num2):
    ''' # doc string
    숫자 2개 더한 후 결과 반환
    :param num1: int
    :param num2: int
    :return: int
    '''
    value = num1 + num2

    return value

#함수 사용하기 = 함수 호출


result = addTwo(10, 20) #이 자리에 value 값
print(result)
