#가변인수 : 유사하거나 동일한 코드 부분 그대로
#       : 인자(인수) 개수만 계속 변경 >> 유동적
#       : *매개변수 => 0
# 키워드 파라미터 함수 = **매개변수 ( 딕셔너리 형태로 저장)
def addTwo(num1, num2=0): #num2 값이 없을시 기본값인 0이 들어간다
    ''' # doc string
    숫자 2개 더한 후 결과 반환
    :param num1: int
    :param num2: int
    :return: int
    '''
    value = num1 + num2

    return value

def addNum(*nums): #*nums 는 여러개 숫자 중복 x 튜플형태로 저장됨 인자
    print(f'nums type : {type(nums)}')
    total = 0
    for num in nums: total += num # 한문장이면 뒤에 붙여 써도됨
    return total

print(addNum(10,20,30))
print(addTwo(3))

#함수의 데이터 타입 = class function

print(type(addTwo))

list = [addTwo, addNum]
print(list[0](1,2))

