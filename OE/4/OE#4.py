print ("OE#4\nArdent Azrael Sayson\nBSIT2B\n")

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.defend(self.power)
        print(f"{self.name} attacks {target.name} for {self.power} damage!\n")
        print(f"{target.name}'s remaining health: {target.health}\n")

    def special_move(self):
        pass

    def defend(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2


class Mage(Character):
    def special_move(self, target):
        print(f"{self.name} casts Fireball!")
        target.defend(100)
        print(f"{target.name}'s remaining health: {target.health}")


class Archer(Character):
    def special_move(self, target):
        print(f"{self.name} shoots a Piercing Arrow!")
        target.defend(50)
        print(f"{target.name}'s remaining health: {target.health}")


class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50
        print(f"{self.name}'s health after roar: {self.health}")


# Create objects for each class
warrior = Warrior("Warrior", 300, 50)
mage = Mage("Mage", 250, 30)
archer = Archer("Archer", 200, 40)
monster = Monster("Monster", 500, 20)

# Simulate a battle
while monster.health > 0:
    warrior.attack(monster)
    warrior.special_move()
    
    mage.attack(monster)
    mage.special_move(monster)
    
    archer.attack(monster)
    archer.special_move(monster)
    
    if monster.health > 0:
        monster.attack(warrior)
        monster.special_move()
        
        monster.attack(mage)
        monster.special_move()
        
        monster.attack(archer)
        monster.special_move()
