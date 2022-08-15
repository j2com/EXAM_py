import os
DIR_PATH = '../AccountBook2/'
dataList = os.listdir(DIR_PATH)
inputMon = input("월을 입력하시오(ex 00) : ")
n3 = int(input("일을 입력하시오(ex 0) : "))
n4 = int(input("일을 입력하시오(ex 0) : "))
def day1_plus(n3):
    for mon in dataList:
        if mon[5:7] == inputMon:
            with open(DIR_PATH+"/plus_use/"+inputMon, "r", encoding="utf8") as f1:
                sum1 = 0
                for i in range(0, n3-1):
                    data1 = f1.readline()

                    for pay1 in data1[1:2]:
                        sum1 += int(pay1)
                return sum1
def day2_plus(n4):
    for mon in dataList:
        if mon[5:7] == inputMon:
            with open(DIR_PATH+"/plus_use/"+"2022."+inputMon, "r", encoding="utf8") as f1:
                sum2 = 0
                for i in range(0, n4):
                    data1 = f1.readline().split(",")

                    for pay1 in data1[1:2]:
                        sum2 += int(pay1)
                return sum2
