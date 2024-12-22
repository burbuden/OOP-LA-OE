print ("LA#14\nArdent Azrael Sayson\nBSIT-2B\n")

class SpiderMan:
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = age

    def describeSpiderman(self):
        return(f"This variant of Spider-man is played by {self.name} and the actor is currently {self.age} years old.")


class Tobey(SpiderMan):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()

class Andrew(SpiderMan):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()

class Tom(SpiderMan):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()


spdrmn1 = Tobey("tobey", 49, "Spider-Man (Sam Raimi's Trilogy)")
spdrmn2 = Andrew("andrew", 41, "The Amazing Spider-Man")
spdrmn3 = Tom("tom", 28, "Spider-Man (Home Trilogy)")

print("Movie:", spdrmn1.movieTitle, "\nInfo:" , spdrmn1.describeSpiderman(),"\n")
print("Movie:", spdrmn2.movieTitle, "\nInfo:" , spdrmn2.describeSpiderman(),"\n")
print("Movie:", spdrmn3.movieTitle, "\nInfo:" , spdrmn3.describeSpiderman(),"\n")
