print ("OOP LA#7\nArdent Azrael Sayson\nBSIT-2B\n")
class Car: 
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def carInfo(self):
        return f"The car is from {self.brand} and showcases a color of {self.color}\n"
        
car1 = Car("Toyota", "Black")
print (car1.carInfo())
car1.color = "Red"

car2 = Car("Mazda", "Yellow")
print (car2.carInfo())
print (car1.carInfo())
