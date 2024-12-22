print("LA#22\nArdent Azrael Sayson\nBSIT2B\n")

class PartyMain:

    dish1 = None
    dish2 = None
    _sdish3 = None
    __sdish4 = None


    def __init__(self,partytheme,dish1,dish2,sdish3,sdish4):
        self.partytheme = partytheme.upper()
        self.dish1 = dish1
        self.dish2 = dish2
        self._sdish3 = sdish3
        self.__sdish4 = sdish4

    def displayTheme(self):
        print(f'''THEME: {self.partytheme}''')

    def displayFoods(self):
        print (f'''Dish 1: {self.dish1}
Dish 2: {self.dish2}''')

    def _displaySdish(self):
        print(f'''Surprise Side Dish: {self._sdish3}''')

    def __revealMainSdish(self):
        print(f'''CHARAAAN: {self.__sdish4}\n''')


    def AuntComesIn(self):
        self.__revealMainSdish()

    def dispEverything(self):
        self.displayTheme()
        self.displayFoods()
        self._displaySdish()
        self.__revealMainSdish()

class PartySub(PartyMain):
    def __init__(self,partytheme,dish1,dish2,sdish3,sdish4):
        super().__init__(partytheme,dish1,dish2,sdish3,sdish4)

    def BrotherComesIn(self):
        self._displaySdish()

T1 = PartySub("Children's Birthday", "Hotdog and mallows on stick", "Spaghetti", "Ice Cream",
            "Cake")
T2 = PartySub("Year End", "Chicken Wings", "Fries", "Mango Float", "Ice Cream Cake")
T3 = PartySub("Watch Party", "Chips", "Nachos","French Fries", "Pizza")
T1.dispEverything()
T2.dispEverything()
T3.dispEverything()

T1.BrotherComesIn()
#T1.__revealMainSdish