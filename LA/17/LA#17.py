print("LA#17\nArdent Azrael Sayson\nBSIT-2B\n")

class Players:
    def __init__(self,name,hp,atkpwr):
        self.name = name
        self.hp = hp
        self.atkpwr = atkpwr
    
    def attack(self,target):
        target.hp -= self.atkpwr
        if target.hp <= 0:
            print(f"{target.name} has fainted!")
        else:
            pass
        
    def __str__(self):  
        return f"{self.name} current health pool is {self.hp}"
      
    def heal(self,amount):
        self.hp += amount
        
Unga = Players("Unga", 100, 13)
Boonga = Players("Boonga", 14, 12)

Unga.attack(Boonga)
print(Boonga)
Boonga.attack(Unga)
print(Unga)
Unga.attack(Boonga)