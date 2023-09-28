
class Animal:
    def __int__(self,name,sound):
        self.name = name
        self.sound=sound

    def description(self):
        return f"I'm {self.name} and i {self.sound}."

class cat(Animal):

    def __init__(self,name,sound,mytype):
        super().__int__( name, sound)
        self.mytype = mytype


    def details(self):
        a= Animal.description(self)
        print(f" {a} I am {self.mytype}")

class dog(Animal):

    def __init__(self,name,sound,mytype):
        super().__int__( name, sound)
        self.mytype = mytype


    def details(self):
        a= Animal.description(self)
        print(f" {a} I am {self.mytype}")

cat1 = cat("Cat","Meow", "pet")
dog1 = dog("Dog","Bark", "pet")
cat1.details()
dog1.details()

# class vechile:
#     def __int__(self,brand,colour):
#         self.brand = brand
#         self.colour=colour

#     def description(self):
#         print(f"Brand: {self.brand}")
#         print(f"Colour: {self.colour}")
#
# class car(vechile):
#
#     def __init__(self,brand,colour,year):
#         super().__int__( brand, colour)
#         self.year = year
#
#
#     def details(self):
#         print("Car Details:")
#         print(f"Year: {self.year}")
#
# car1 = car("Hyundai","Red", 2023)
# car1.details()
# car1.description()




