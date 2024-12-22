print("LA#24\nArdent Azrael Sayson\nBSIT2B\n")

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
    
class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
        
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")
        
class Archer(GameCharacter):
    def attack (self):
        print("Shoots an arrow!")
        
class Healer(GameCharacter):
    def attack(self):
        print("Bonks you with a healing stick!")
        
Garen = Warrior()
Ionia = Mage()
Kaun = Archer()
Taric = Healer()

Garen.attack()
Ionia.attack()
Kaun.attack()
Taric.attack()

