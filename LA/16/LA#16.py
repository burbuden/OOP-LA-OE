print("LA#16\nArdent Azrael Sayson\nBSIT-2B\n")

class Appliance:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def info(self):
        print (f"Brand: {self.brand}\nModel: {self.model}")
    def operate(self):
        print(f"The appliance is now operating!\n")
        
class WashingMachine(Appliance):
    def operate(self):
        print(f"The washing machine is now washing the laundry!\n")
        
class Refrigerator(Appliance):
    def operate(self):
        print(f"The refrigerator is now prolonging the food's shelf life!\n")
        
class Microwave(Appliance):
    def operate(self):
        print(f"The microwave is now heating the food!\n")
    
wm = WashingMachine("Panasonic", "FD85X1HRM")
r = Refrigerator("Condura", "Personal Two-Door Refrigerator")
m = Microwave("Toshiba", "MM-EG25P(BK) Microwave Oven")

def callEm(appies):
    appies.info(), appies.operate()
    
for calling in [wm, r, m]:
    callEm(calling)
