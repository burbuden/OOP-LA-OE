print("LA#12\nArdent Azrael Sayson\n2B\n")

class Toy:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def infoToy(self):
        print(f"Name:{self.name}\nPrice: {self.price}\n")

class Car(Toy):
    def __init__(self,name, price):
        super().__init__(name, price)
    
class Gundam(Toy):
  def __init__(self,name, price):
        super().__init__(name, price)
        
        
carToy = Car("1997 Johnny Lightning Speed Racer Mach 5", "Php 838.77")
trnsfToy = Gundam("Gundam 5063057 PG 1/60 Gundam Exia", "Php 13,999.00")

carToy.infoToy()
trnsfToy.infoToy()
