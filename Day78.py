# In this we will be learning about the single inheritance

class human:
    def __init__(self, feature):
        self.feature = feature

    def features(self):
        print(f"I can {self.man}")


class women(human):
    def __init__(self, feature):
        human.__init__(self, feature="walk")
        self.feature = feature

    def features(self):
        print(f"I can {self.feature}")

    def run(self):
        print("I can also Run!")


misti = women("walk")
print(misti.run())


# *****************************************************************************************************************


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()


# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
class cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self, name, species="cat")
        self.breed=breed

    def make_sound(self):
        print("Meows!")


cat = cat("cat","persian cat")
cat.make_sound()
