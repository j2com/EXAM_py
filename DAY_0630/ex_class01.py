class Spagetti:

    def __init__(self, noodle, source, vegetable):
        self.noodle = noodle
        self.source = source
        self.vegetable = vegetable

    def heatWater(self, water):

        print(f'{water} 을 끓인다')

    def makeNoodle(self):

        print(f'{self.noodle}을 삶는다')

    def makeVegetable(self, knife):

        print(f'{self.vegetable} 을 {knife}로 손질한다')
        print(f'{self.vegetable} 을 {self.noodle}에 넣는다')

    def inputSource(self):

        print(f'{self.source} 를 {self.noodle}에 넣는다')

    def showUi(self):

        print('******* 스파게티 조리법 *******')

spa = Spagetti('noodle', 'source', 'vegetale' )
spa.showUi()
spa.heatWater("water")
spa.makeNoodle()
spa.makeVegetable("식칼")
spa.inputSource()