#-----------------------------------------------------------------------------------------------------
# Exception Handling : 예외처리
# 프로그램 실행 시 발행하는 오류(Error)에 대한 처리
# 오류가 발생해도 프로그램 중단하지 않고 실행시키는 것
#----------------------------------------------------------------------------------------------------
try:
    num1, num2 = 10, 0

    print(f'{num1}/{num2} = {num1/num2}')

    print("END")
except Exception as ex:
    print("에러발생", ex)

finally:
    # 오류 발생 여부 상관 없음
    # 무조건 실행
    print('finallyyyyy')
