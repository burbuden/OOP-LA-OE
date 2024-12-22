print ("OOP LA#2\nArdent Azrael Sayson\nBSIT-2B\n")

class MLBB: 
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    # def Desc(self):
    #     print (f"{self.name}'s role is {self.role}.")
        
    def __str__(self):
        return "Ruby's's role is fighter."
        
main = MLBB("Ruby", "Fighter")
print(main.name , main.role)
# print(main.Desc())
print(main)