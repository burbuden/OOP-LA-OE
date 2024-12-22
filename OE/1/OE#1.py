print ("OE#1\nArdent Azrael Sayson\nBSIT2B\n")

class mlbb:
    def __init__(self, name, role,  basic_atk, playstyle, diff, lane):
        self.name = name
        self.role = role
        self.basic_atk= basic_atk
        self.playstyle = playstyle
        self.diff= diff
        self.lane = lane

    def desc_hero(self):
        return f'''\f\fDescription: \f{self.name}'s role is a {self.role} that excels at {self.playstyle} playstyle.'''

    def lane_hero(self):
        return f'''\f\f{self.name} is being played at {self.role} lane.'''
    def __str__(self):
        return f"\f\f{self.name} is a {self.diff} difficulty hero"
    
format = 'Hero name:'
format2 = '\f ------------ \fRole:'
format3= '\f ------------ \fStats \fBasic Attack:'
formatsep = '\f ' * 2

mlbbMage1= mlbb('Luo Yi', 'Mage', 90, 'Poke/Burst', '⭐⭐⭐⭐', 'Mid' )
mlbbFighter1 = mlbb('Aldous', 'Fighter', 134, 'Engage/All-in', '⭐⭐⭐', 'Exp')
mlbbPwetpwetpasok1 = mlbb('Fanny', 'Assassin', 112, 'Picks/Burst', '⭐⭐⭐⭐⭐', 'Core')
mlbbMM1 = mlbb('Jinx', 'Marksman', 148, 'DPS', '⭐', 'Gold')
mlbbSP1 = mlbb('Estes', 'Roam', 71, 'Healer/Sustain', '⭐⭐', 'Roam')

print(format, mlbbMage1.name, format2, mlbbMage1.role, format3, 
      mlbbMage1.basic_atk, mlbbMage1.desc_hero(), mlbbMage1, mlbbMage1.lane_hero(), formatsep)
print(format , mlbbFighter1.name, format2, mlbbFighter1.role, format3, 
      mlbbFighter1.basic_atk, mlbbFighter1.desc_hero(), mlbbFighter1, mlbbFighter1.lane_hero(), formatsep)
print(format , mlbbPwetpwetpasok1.name, format2, mlbbPwetpwetpasok1.role, format3, 
     mlbbPwetpwetpasok1.basic_atk, mlbbPwetpwetpasok1.desc_hero(), mlbbPwetpwetpasok1, mlbbPwetpwetpasok1.lane_hero(), formatsep)
print(format , mlbbMM1.name, format2, mlbbMM1.role, format3, 
      mlbbMM1.basic_atk, mlbbMM1.desc_hero(), mlbbMM1, mlbbMM1.lane_hero(), formatsep)
print(format , mlbbSP1.name, format2, mlbbSP1.role, format3, 
      mlbbSP1.basic_atk, mlbbSP1.desc_hero(), mlbbSP1, mlbbSP1.lane_hero(), formatsep)