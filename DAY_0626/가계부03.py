import os
DIR_PATH = "../account/"

# (1) 수입/지출 입력 클래스
class Flow_money:

    def __init__(self,date,money,category="1"):
        self.date=date
        self.money=money
        self.category=category

# 지출 입력 ( 날짜, 금액, 카테고리 )
    def money_out(self):
        with open(DIR_PATH+ "use", "a", encoding="utf8") as f:
            f.write("2022" + self.date+" ")
            f.write(self.money+" ")
            f.write(self.category+" \n")

# 수입 입력( 날짜, 금액 )
    def money_in(self):
        with open(DIR_PATH + "plus", "a", encoding="utf8") as f:
            f.write("2022" +self.date + " ")
            f.write(self.money + "\n")

# # 저축 확인 및 입력 ( 날짜, 금액 )
#     def money_save(self):
#         with open(DIR_PATH + "save", "a", encoding="utf8") as f:
#             f.write(self.date + " ")
#             f.write(self.money + "\n")

# (3) 1일 지출 / 1달 지출 / 카테고리별 비중 클래스
class Moneyinfo:

    def __init__(self,filename,search_mode="1",category="1"):
        self.filename = filename
        self.search_mode = search_mode
        self.category = category

    def cal_present(self,useAddr):
        total1 = 0
        total2 = 0
        with open(DIR_PATH + self.filename, "r", encoding="utf8") as f:
            while True:
                line = f.readline().split()
                if not line : break
                total1 = total1 + int(line[1])
        with open(DIR_PATH + useAddr, "r", encoding="utf8") as f:
            while True:
                line = f.readline().split()
                if not line: break
                total2 = total2 + int(line[1])
        print(total1-total2)

    def cal(self):
        total = 0
        with open(DIR_PATH + self.filename, "r", encoding="utf8") as f:
            while True:
                line = f.readline().split()
                if not line: break
                if len(self.search_mode) == 2:
                    if line[0][:2] == self.search_mode:
                        total = total + int(line[1])
                elif len(self.search_mode) == 5:
                    if line[0] == self.search_mode:
                        total = total + int(line[1])
                elif self.search_mode == "S":
                        total = total + int(line[1])
            print(f"{self.search_mode}의 총 금액 : {total}원")
        if self.category == 0:
            pass
        elif total>0:
            total1 = 0
            total2 = 0
            total3 = 0
            with open(DIR_PATH + "use", "r", encoding="utf8") as f:
                while True:
                    line = f.readline().split()
                    if not line: break
                    if line[2] == "식비" and (line[0][:2] == self.search_mode or line[0] == self.search_mode):
                        total1 = total1 + int(line[1])

                    elif line[2] == "고정지출" and (line[0][:2] == self.search_mode or line[0] == self.search_mode):
                        total2 = total2 + int(line[1])

                    elif line[2] == "특수비용" and (line[0][:2] == self.search_mode or line[0] == self.search_mode):
                        total3 = total3 + int(line[1])

                print(f"{self.search_mode}의 (식비)카테고리 총 지출 : {total1}원 ({round(total1 / total, 2) * 100})%")
                print(f"{self.search_mode}의 (고정지출)카테고리 총 지출 : {total2}원 ({round(total2 / total, 2) * 100})%")
                print(f"{self.search_mode}의 (특수비용)카테고리 총 지출 : {total3}원 ({round(total3 / total, 2) * 100})%")
                print()


# (4) 초기 폴더 생성 함수 : use.txt를 저장할 폴더가 없을 때, 초기 폴더 생성.
def makeFile():
    if not os.path.exists(DIR_PATH):
        os.makedirs("")
# ]------------------------------------------------------------------------------------------------------------
def day1(n1):
    dataList = os.listdir(DIR_PATH)
    for mon in dataList:
        if mon[:2] == inputMon:
            with open(DIR_PATH+inputMon, "r", encoding="utf8") as f1:
                sum1 = 0
                for i in range(0, n1-1):
                    data1 = f1.readline().split()

                    for pay1 in data1[1:2]:
                        sum1 += int(pay1)
                return sum1
def day2(n2):
    dataList = os.listdir(DIR_PATH)
    for mon in dataList:
        if mon[:2] == inputMon:
            with open(DIR_PATH+inputMon, "r", encoding="utf8") as f1:
                sum2 = 0
                for i in range(0, n2):
                    data1 = f1.readline().split()

                    for pay1 in data1[1:2]:
                        sum2 += int(pay1)
                return sum2

def day3(n3):
    dataList = os.listdir(DIR_PATH)
    for mon in dataList:
        if mon[:2] == inputMon:
            with open(DIR_PATH+inputMon, "r", encoding="utf8") as f1:
                sum3 = 0
                for i in range(0, n3-1):
                    data1 = f1.readline().split()

                    for pay1 in data1[1:2]:
                        sum3 += int(pay1)
                return sum3
def day4(n4):
    dataList = os.listdir(DIR_PATH)
    for mon in dataList:
        if mon[:2] == inputMon:
            with open(DIR_PATH+inputMon, "r", encoding="utf8") as f1:
                sum4 = 0
                for i in range(0, n4):
                    data1 = f1.readline().split()

                    for pay1 in data1[1:2]:
                        sum4 += int(pay1)
                return sum4



# [ 2. 실행 ]--------------------------------------------------------------------------------------
makeFile()   # 폴더 없을 시, 생성하는 코드

# 현재 총 예산
print(" 현재 예산 현황")
M=Moneyinfo("plus")
M.cal_present("use")
while True:  # 메뉴 선택
    print("===== 가계부 =====")
    print("1. 수 입  입 력")
    print("2. 지 출  입 력")
    print("3. 저 축  입 력")
    print("4. 1일 지출 검색")
    print("5. 1달 지출 검색")
    print("6.기간별 지출 검색")
    print("7. 종        료")
    print("=" * 18)
    choice = input("번호 선택 : ")

# 1.수입 입력하기
    if choice=="1":
        date_input = input("입력 날짜:(ex.06.25): ")
        money_input = input("지출 금액:(ex.10000): ")
        print(" [ 수입 총액 ]")
        F=Flow_money(date_input,money_input)
        F.money_in()

# 2.지출 입력하기
    elif choice == "2":
        date_input = input("입력 날짜:(ex.06.25): ")
        money_input = input("지출 금액:(ex.10000): ")
        category_input = input("카테고리(식비/고정지출/특수비용): ")
        print(" [ 지출 총액 ]")
        F=Flow_money(date_input, money_input, category_input)
        F.money_out()

# 3.저축 확인 및 입력하기.
    elif choice == "3":
        print("======= 저축 ========")
        print(" 1. 저축 항목 생성 ")
        print(" 2. 금액 입력 하기 ")
        print("=== 현재 저축 현황 ====")
        # save_choice = input("번호 선택:")
        # if save_choice == "1":
        #     save_name = input("생성할 저축 항목 이름: ")
        #     with open(DIR_PATH+save_name,"a",encoding="utf8") as f:
        #         f.write("")
        #
        # date_input = input("입력 날짜:(ex.06.25): ")
        # save_input = input("입력 금액:(ex.10000): ")
        # print(" [ 저축 총액 ]")
        # F = Flow_money(date_input, save_input)
        # F.money_save()
        # M = Moneyinfo("save","S",0)
        # M.cal()

# 4.해당 날짜 지출 검색
    elif choice == "4":
        date_input = input("일 입력(ex.06.23): ")
        M = Moneyinfo("use",date_input)
        M.cal()

# 5.해당 월 지출 검색
    elif choice == "5":
        month_input = input("월 입력(ex.01): ")
        M = Moneyinfo("use",month_input)
        M.cal()

# 6. 기간별 지출 검색
    elif choice == "6":
        inputMon = input("월을 입력하시오(ex 00) : ")
        n3 = int(input("일을 입력하시오(ex 0) : "))
        n4 = int(input("일을 입력하시오(ex 0) : "))
        print(day1(n3) - day2(n4))
# 7.종료하기
    elif choice == "6":
        break

# 8.재입력
    else:
        print("1,2,3,4 중 다시 입력해주세요.")