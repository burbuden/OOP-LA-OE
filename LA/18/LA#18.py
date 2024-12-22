print("LA#19\nArdent Azrael Sayson\nBSIT2B\n")

class MyFav:
    def __init__(self, recipeName, flour, bakingSoda, salt, butter, sugar1, sugar2, egg, yolk,
                vanillaExtract, espressoPowder, toppings1, toppings2):
        self.recipeName = recipeName
        self.flour = flour
        self.bakingSoda=bakingSoda
        self.salt=salt
        self.butter=butter
        self.sugar1=sugar1
        self.sugar2=sugar2
        self.egg=egg
        self.yolk=yolk
        self.vanillaExtract=vanillaExtract
        self.espressoPowder=espressoPowder
        self.toppings1=toppings1
        self.toppings2=toppings2
        
    def __str__(self):
        return f'''{self.recipeName}
        Ingredients: 
        220g of {self.flour}
        1/2 tsp of {self.bakingSoda}
        1/2 tsp of {self.salt}
        140g of {self.butter}
        150g of {self.sugar1}
        100g of {self.sugar2}
        1 large {self.egg}
        1 large {self.yolk}
        2 tsp of {self.vanillaExtract}
        1/2 tsp of {self.espressoPowder}
        {self.toppings1}
        {self.toppings2}
        '''
chocoChips = MyFav("Chocolate Chips Cookies", "Maya All-Purpose Flour", "Arm and Hammer Pure Baking Soda",
"Mccormick Iodized Salt", "Queensland Butter", "Equal Brown Sugar", "Hermano Refined Sugar",
"Egg", "Egg Yolk", "Mccormick Pure Vanilla", "DeLallo Instant Espresso Powder",
"Goya Chocolate Chips", "Goya Hazelnut Spread")

YinAndYangCookies = MyFav("Yin And Yang Cookies", "Maya All-Purpose Flour", "Arm and Hammer Pure Baking Soda",
"Mccormick Iodized Salt", "Queensland Butter", "Equal Brown Sugar", "Hermano Refined Sugar",
"Egg", "Egg Yolk", "Mccormick Pure Vanilla", "DeLallo Instant Espresso Powder",
"Hershey White Chocolate Chips", "Goya Dark Chocolate Spread")

OkraCookies = MyFav("Okra Cookies", "Maya All-Purpose Flour", "Arm and Hammer Pure Baking Soda",
"Mccormick Iodized Salt", "Queensland Butter", "Equal Brown Sugar", "Hermano Refined Sugar",
"Egg", "Egg Yolk", "Mccormick Pure Vanilla", "DeLallo Instant Espresso Powder",
"Okra", "Wasabi")

print (chocoChips)
print (YinAndYangCookies)
print (OkraCookies)
