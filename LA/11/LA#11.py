print("LA#11\nArdent Azrael Sayson\n2B\n")

class Phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def DescribePhone(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\n")

class Android(Phone):
    def __init__(self,brand,model):
        Phone.__init__(self,brand,model)
    
class iPhone(Phone):
  def __init__(self,brand,model):
        Phone.__init__(self,brand,model)
        
        
Android1 = Android("Nokia", "3310")
Apple1 = iPhone("iPhone", "13")

Android1.DescribePhone()
Apple1.DescribePhone()
