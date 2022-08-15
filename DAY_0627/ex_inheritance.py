#-----------------------------------------------------------------------------
# 상속 -> 기존 클래스의 모든 것을 가져다가 사용하는 것 => 재사용 또는 확장
#
# 표현 : class 클래스명( 클래스명) :
# -----------------------------------------------------------------------------

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f'A => {self.x}, {self.y}')

class B(A):

    def calc(self):
        print(self.x *self.y)

b = B(5,3)
b.display()
b.calc()

class C(B):
    def add(self):
        print(self.x + self.y)
    #오버라이딩 : 상속 클래스 리모델링시 자식 클라스 먼저
    def cal(self):
        print(self.x + self.y,self.x - self.y,self.x * self.y,self.x / self.y)

c = C()
