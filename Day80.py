# In this we will be learning about the multilevel inheritance


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed: {self.breed}")


class GermanShepherd(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="German Shepherd")
        self.color = color

    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color: {self.color}")


o = GermanShepherd("Tommy", "Red")
o.showDetails()
