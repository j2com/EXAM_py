#키워드 파라미터
#기 능 : 평균 구하는 함수
#함수명 : getAvg
#파라미터 :과목명 - 점수 유동적 >> **subjects
#가변인자 함수 > 매개변수 0개 ~ n개
#리턴값 : 평균 --- float

def getAvg(**subjects):
    print(f'subjects type : {type(subjects)}')
    values=subjects.values()
    total = 0
    print(f'{total}')
    for value in values: total += value
    return total / len(values) if len(values)>0 else False


print(getAvg(국어=12, 영어=98, 수학=88)) #키워드 파라미터 1. 호출수 따옴표 쓰지 않는다! 2. 키 자리 숫자 불가!
print(getAvg())

