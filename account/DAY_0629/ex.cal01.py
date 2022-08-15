class Calculator:

    def __init__(self, maker, color, *data):
        self.maker = maker
        self.color = color
        self.data = data

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def plus(self):
        sum = self.data[0]
        for i in range(1, len(self.data)):
            sum = sum + self.data[i]
        return sum

    def minus(self):
        minus = self.data[0]
        for i in range(1, len(self.data)):
            minus = minus - self.data[i]
        return minus

    def multi(self):
        multi = self.data[0]
        for i in range(1, len(self.data)):
            multi = multi * self.data[i]
        return multi

    def div(self, *data):
        div = self.data[0]
        for i in range(1, len(self.data)):
            div = div / self.data[i]
        return div

    def showUi(self):
        print('*******계산기*******')
        print('     1. 덧셈')
        print('     2. 뺄셈')
        print('     3. 곱셈')
        print('     4. 나눗셈')
        print('     5. 종료')
        print('********************')

def getnumbers():
    nums = []
    while True:
        num = input()
        if num in ['q', 'Q']:
            break

        else:
            nums.append(int(num))

def playApp():
    calc = Calculator('sharp', 'pink')
    calc.showUi()
    while True:
        select = input("번호를 입력하세요 : ")
        if select == '5':
            break
        elif select == '1':
            calc.setData(getnumbers())
            print(calc.plus())
        elif select == '2':
            calc.setData(getnumbers())
            print(calc.minus())
        elif select == '3':
            calc.setData(getnumbers())
            print(calc.multi())
        elif select == '4':
            calc.setData(getnumbers())
            print(calc.div())

playApp()