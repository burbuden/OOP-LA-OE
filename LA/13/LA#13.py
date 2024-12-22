print("LA#13\nArdent Azrael Sayson\n2B\n")

class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        
    def info(self):
        print(f"Name: {self.name}\nType: {self.type}\n")

class Fish(Animal):
    def __init__(self,name,type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim
        if can_swim == True:
            print (f"Yes")
        else:
            print(f"Nop")
    
    
fish1= Fish("Tilapia", "Fish", True)

fish1.info()
print("But can it swim?", fish1.can_swim)