print ("OOP LA#9\nArdent Azrael Sayson\nBSIT-2B\n")

class Car: 
    def __init__(self, brand, color, material):
        self.brand = brand
        self.color = color
        self.material = material
        
    def __str__(self):
        return f"The car is from {self.brand} and showcases a color of {self.color} made out of {self.material}."
        
car1 = Car("Toyota", "Black", "Tungsten and Carbon")
print(car1)

del car1
print(car1)
