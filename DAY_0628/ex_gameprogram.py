#------------------------------------------------------------------------------------
# 벽돌깨기 프로그램 만들기
# ----------------------------------------------------------------------------------
# 게임하는 사람들의 정보들
nickname = ''
level = 0
score = 0
lanking = 0
player1 = None
player2 = None

# 게임하는 사람의 정보 입력 받기 -------------------------------------
# 함 수 명 : setPlayer
# 파라미터 : 없음
# 반 환 값 : 없음
def setPlayer():
    global player1, player2
    nickname = input('닉네임 : ').split()
    if player1 == None:
        player1=player(nickname)

#-----------------------------------------------------------------------------
# 메뉴 출력하기
# 함 수 명 : displayName
# 파라미터 : 없음
# 반환 값 : 없음
#---------------------------------------------------------------------------
def displayMenu():
    print('1.회원가입')
    print('2.게임시작')
    print('3.랭킹보기')
    print('4.종료')
#----------------------------------------------------------------------------
while True:
    displayMenu()
    select = input()

    if select == '4': #파일에 기록하고 종료

        break
    elif select == 1:
        setPlayer()


class player:
    def __init__(self, nickname, level = 0, score = 0, lanking=0):
        self.nickname = nickname
        self.level = 0
        self.score = 0
        self.lanking = 0

    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽기 하는 메서드
    #set메서드 - get메서드
    def setlevel(self, level):
        self.level = level

    def setScore(self, score):
        self.score = score

    def setLanking(self, lanking):
        self.lanking = lanking

    def update(self, level, score, lanking):
        self.level = level
        self.score = score
        self.lanking = lanking

    def getNickname(self): return  self.nickname

    def getScore(self): return self.score

    def getLanking(self): return self.lanking


