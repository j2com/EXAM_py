#--------------------------------------------------------
#사용자 정의 클래스 => 학생을 표현하는 데이터 타입
#---------------------------------------------
# 특징!성질!외형! => 변수 -- 필드/속성(filde/attribute)
                   #교복, 급식, 학교, 담임, 성적, 학년
# 역할/기능      => 함수 -- 메서드(Method)
                    #공부한다, 학교에 간다, 시험친다
#-------------------------------------------------------
#클래스명 => student
#속성 => 학번, 학교, 학년, 석차
#기능 => 공부한다, 시험친다
class Student:
    #클래스 변수 -> 모든 인스턴스가 함께 사용함
    school = '대구중학교'
    #인스턴스(객체) 생성시 초기화 #self라는 메모리 생김
    def __init__(self, stdNum, yearNum, grade):
        self.stdNum = stdNum   #객체내의 인스턴스들
        self.yearNum = yearNum
        self.grade = grade
#클래쓰의 역할/기능 메서드
#000이 무슨 과목을 공부한다
    def study(self, subject):
        print(f'{self.stdNum}은 {subject} 과목을 공부한다')
#000이 무슨 시험을 친다
    def test(self, subject):
        print(f'{self.stdNum}은 {subject}과목을 공부한다')

    def displayInfo(self):
        print(f'학교 : {Student.school}') #클래스 전역 변수라
        print(f'학번 : {self.stdNum}')
        print(f'학년 : {self.yearNum}')

#객체 즉 student 인스턴스 생성

Stt1 =  Student('std001',  1, 10)
Stt2 =  Student('std002',  1, 8)
Stt3 =  Student('std101',  3, 14)

    #학생정보 출력 가능 -------------------------------------------------------
    #학번, 학년, 학교 정보 출력
