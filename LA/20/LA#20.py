print("LA#20\nArdent Azrael Sayson\nBSIT2B\n")

class MyFav:
    def __init__(self, flour, bakingSoda, salt, butter, sugar1, sugar2, egg, yolk,
                vanillaExtract, espressoPowder, toppings1, toppings2):
        self.__flour = flour
        self.__bakingSoda=bakingSoda
        self.__salt=salt
        self.__butter=butter
        self.__sugar1=sugar1
        self.__sugar2=sugar2
        self.__egg=egg
        self.__yolk=yolk
        self.__vanillaExtract=vanillaExtract
        self.__espressoPowder=espressoPowder
        self.__toppings1=toppings1
        self.__toppings2=toppings2
        
    def __str__(self):
        return f'''Ingredients: 
        220g of {self.__flour}
        1/2 tsp of {self.__bakingSoda}
        1/2 tsp of {self.__salt}
        140g of {self.__butter}
        150g of {self.__sugar1}
        100g of {self.__sugar2}
        1 large {self.__egg}
        1 large {self.__yolk}
        2 tsp of {self.__vanillaExtract}
        1/2 tsp of {self.__espressoPowder}
        {self.__toppings1}
        {self.__toppings2}
        '''
    def EspressoChecker (self,ferson):
        print (f"{ferson}: May kape ba itu?")
        if ferson == "Ash":
            return "Response: No kape"
        else:
            return self.__espressoPowder

chocoChips = MyFav("Maya All-Purpose Flour", "Arm and Hammer Pure Baking Soda",
"Mccormick Iodized Salt", "Queensland Butter", "Equal Brown Sugar", "Hermano Refined Sugar",
"Egg", "Egg Yolk", "Mccormick Pure Vanilla", "DeLallo Instant Espresso Powder",
"Goya Chocolate Chips", "Goya Hazelnut Spread")

print (chocoChips)

print (chocoChips.EspressoChecker("Ash"))