#--------------------------------------------------------------
# 현대 자동차를 표현하는 데이터 타입 즉 class 생성
# 클래스명 : car
# 속성/특징 : 제조사, 차번호, 차종류, 색상
# 역할/기능 : 이동한다, 정지한다, 차정보 출력한다.
#           -> 이동한다 :  => 000 자동차가 xx에서 xx로 간다 xx = 매번 바뀌기에 파라미터로 받아야함
#            -> 정지한다 :  => 000 자동차가 xxx에 정지한다
#           -> 차정보를 출력한다 => 제조사, 차종류, 차번호
#--------------------------------------------------------------

class Car:
    carBrand = '현대'
    def __init__(self, carNum, carName, carCol): #
                  #만들어 놓은 주소(self) 안에 넣는 과정
        self.carNum = carNum
        self.carName = carName
        self.carCol = carCol

    def carMove(self, loc1, loc2):
        print(f'{Car.carBrand} {self.carNum} 자동차가 {loc1} 에서 {loc2}로 간다')

    def carStop(self, des):
        print(f'{Car.carBrand} 자동차가 {des}에 정지한다.')

    def displayInfo(self):
        print(f'차 번호 : {self.carNum}')
        print(f'차 종류 : {self.carName}')
        print(f'차 색상 : {self.carCol}')
#----------------------------------------------------------------여기 까지 객체만 생성
#자동차 데이터 저장 => 자동차 인스턴스 생성
myCar = Car(1234,'suv','hotpink')  #init 파라미터 넣으라고 뜸
myCar.carMove("경북대", "경주")
myCar.displayInfo()

# 정수 10 => car 데이터 10개 저장
nums = []
for n in range(10): nums.append(n*10)

cars = []
for n in range(10):
    num, type, color = input("차번호, 차종류, 차색상 : ").split()
    cars.append(Car(num, type, color))

for Car in cars:
    print((f'{Car.carNum}'))
    Car.displayInfo()