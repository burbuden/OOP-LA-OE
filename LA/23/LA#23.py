print("LA#23\nArdent Azrael Sayson\nBSIT2B\n")

class AnimeCharacter:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
        
        
    def introduce(self, info):
        def character_intro(*args, **kwargs):
            print("?: Introducing!")
            info(*args, **kwargs)
            print(f"{self.name}: I am {self.name} and I can {self.ability}\n")
            print("?: And they will be a part of the Isekai Quartet!\n")
        return character_intro

char1 = AnimeCharacter("Natsuki Subaru", "Return by Death")

@char1.introduce
def fromwhere(Anime):
    print(f"?: From one of the cast from {Anime}!\n")
    
fromwhere("ReZero")

print("LA#24\nArdent Azrael Sayson\nBSIT2B\n")

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass