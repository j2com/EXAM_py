import os
DIR_PATH = "../AccountBook2/"
# 검색 키워드에 맞는 해당 월 / 기간의 내역 // 금액 비중 패키지

def period(input1, input2):

    with open(DIR_PATH+"2022.06", "r", encoding="utf8") as f1:   #6월 데이터
        data1 = f1.readline()
        for mon1 in data1:
            if mon1[1] == 'input1':
                    result1 = mon1[2]
            elif mon1[1] == 'input2':
                    result2 = mon1[2]
        minusPay = int(result2) - int(result1)
            # if mon1[5:7] == '06':
            #     with open(DIR_PATH+mon1,mode='r',encoding='utf-8') as f2:
            #         data2 = f2.readline().split()
            #         print(data2)
            #         for mon2 in data2:                      #01 02 03 04
            #             if mon2[1][8:10] == input1:
            #                 result1 = mon2[2]
            #             elif mon2[1][8:10] == input2:
            #                 result2 = mon2[2]
            #         minusPay = int(result2) - int(result1)




# (1) 지출 입력 함수
def addFile(date, money, category):
    with open(DIR_PATH+"info", "a", encoding="utf8") as f:
        f.write(date+" ")
        f.write(money+" ")
        f.write(category+" \n")

# (2-1) 1일 지출 함수 : 총 지출 합계
def search_date(date):
    print(f"[ {date[:2]}월 {date[3:]}일 지출 현황 ]")
    total = 0
    with open(DIR_PATH + "info", "r", encoding="utf8") as f:
        while True:
            line=f.readline().split() # str 형태의 자료를 공백을 기준으로 split하여 list화 시킨다.
            if not line: break        # 읽어올 line 없으면 break
            if line[0] == date:
                total = total + int(line[1])
        print(f"{date}월의 총 지출 : {total}원")

# (2-2) 1일 지출 함수 : 카테고리별 비중
    total1 = 0
    total2 = 0
    total3 = 0
    with open(DIR_PATH + "info", "r", encoding="utf8") as f:
        while True:
            line = f.readline().split()
            if not line: break
            if line[2] == "의" and line[0] == date:
                total1 = total1 + int(line[1])
            elif line[2] == "식" and line[0] == date:
                total2 = total2 + int(line[1])
            elif line[2] == "주" and line[0] == date:
                total3 = total3 + int(line[1])
        print(f"{date}월의 (의)카테고리 총 지출 : {total1}원 ({round(total1 / total, 2) * 100})%")
        print(f"{date}월의 (식)카테고리 총 지출 : {total2}원 ({round(total2 / total, 2) * 100})%")
        print(f"{date}월의 (주)카테고리 총 지출 : {total3}원 ({round(total3 / total, 2) * 100})%")
        print()

# (3-1) 1달 지출 함수 : 총 지출 합계
def search_month(month):
    print(f"[ {month}월 지출 현황 ]")
    total = 0
    with open(DIR_PATH + "info", "r", encoding="utf8") as f:
        while True:
            line=f.readline().split()
            if not line: break
            if line[0][:2] == month:
                total = total + int(line[1])
        print(f"{month}월의 총 지출 : {total}원")

# (3-2) 1달 지출 함수 : 카테고리별 비중
    total1=0
    total2=0
    total3=0
    with open(DIR_PATH + "info", "r", encoding="utf8") as f:
        while True:
            line=f.readline().split()
            if not line: break
            if line[2] == "의":
                total1 = total1 + int(line[1])
            elif line[2] == "식":
                total2 = total2 + int(line[1])
            elif line[2] == "주":
                total3 = total3 + int(line[1])
        print(f"{month}월의 (의)카테고리 총 지출 : {total1}원 ({round(total1/total,2)*100})%")
        print(f"{month}월의 (식)카테고리 총 지출 : {total2}원 ({round(total2/total,2)*100})%")
        print(f"{month}월의 (주)카테고리 총 지출 : {total3}원 ({round(total3/total,2)*100})%")
        print()

# (4) 초기 폴더 생성 함수 : info.txt를 저장할 폴더가 없을 때, 초기 폴더 생성.
def makeFile():
    if not os.path.exists(DIR_PATH):
        os.makedirs("info")

def partPay(payName): # 일별 카테고리 금액

    selectDate = input("")
    categoryName = input("")
    with open(DIR_PATH + "info", "r", encoding="utf8") as f:

        while True:
            line = f.readline().split()
            if not line: break
            if selectDate == line[1]:
                print(line[2])



# [ 2. 실행 ]--------------------------------------------------------------------------------------
makeFile()   # 폴더 없을 시, 생성하는 코드
while True:  # 메뉴 선택
    print("===== 가계부 =====")
    print("1. 지 출  입 력")
    print("2. 1일 지출 검색")
    print("3. 1달 지출 검색")
    print("4. 종        료")
    print("5. 카테고리별 지출 금액")
    print("=" * 18)
    choice = input("번호 선택 : ")

# 1.지출 입력하기
    if choice == "1":
        date_input = input("입력 날짜:(ex.06.25): ")
        money_input = input("지출 금액:(ex.10000): ")
        category_input = input("해당 카테고리(의,식,주): ")
        addFile(date_input, money_input, category_input)

# 2.해당 날짜 지출 검색
    elif choice == "2":
        date_input = input("일 입력(ex.06.23): ")
        search_date(date_input)

# 3.해당 월 지출 검색
    elif choice == "3":
        month_input = input("월 입력(ex.01): ")
        search_month(month_input)

# 4.종료하기
    elif choice == "4":
        break

    elif choice == '6':
        input1, input2 = input().split(",")
        period(input1, input2)

# 5.재입력
    else:
        print("1,2,3,4 중 다시 입력해주세요.")