print("LA#15\nArdent Azrael Sayson\nBSIT-2B\n")


class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        return(f"{self.name} says '{self.sound}'!")

class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        return(f"{self.name} says '{self.sound}'!")

class Bird:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        return(f"{self.name} says '{self.sound}'!")
        
class Fish:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        return(f"{self.name} says '{self.sound}'!")
    
        
        
cat = Cat("Pepper", "Meow")
dog = Dog("Rubert", "Woof")
bird = Bird("Blue", "Caw")
fish = Fish("Nemo", "...")

for yawyaw in [cat,dog, bird, fish]:
    print(yawyaw.speak())
