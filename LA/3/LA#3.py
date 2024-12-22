print ("OOP LA#2\nArdent Azrael Sayson\nBSIT-2B\n")

class MLBB: 
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def Desc(self):
        print ("Ruby's role is fighter.")
        
main = MLBB("Ruby", "Fighter")
print(main.name , main.role)
print(main.Desc())
#print(main)