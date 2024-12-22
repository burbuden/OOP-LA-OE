print("LA#10\nArdent Azrael Sayson\n2B\n")

class Vehicle:
    def __init__(self,brand,model,fuel_type):
        self.brand=brand
        self.model=model
        self.fuel_type = fuel_type
        
    def describeVehicle(self):
        print(f'''Brand: {self.brand}
    Model: {self.model}
    Fuel type: {self.fuel_type}
        ''')

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car1 = Car("Honda", "Odyssey Minivan", "Unleaded Gasoline")
mtr1= Motorcycle("Honda", "Super Cub C125", "Unleaded Gasoline")
mtr2= Motorcycle("Kewei", "E-tric H623", "Electric")

car1.describeVehicle()
mtr1.describeVehicle()
mtr2.describeVehicle()
