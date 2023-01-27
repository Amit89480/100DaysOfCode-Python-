# In this we have learned about the inheritance

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The person name is {self.name} and the person age is {self.age}")



# Here we are inheriting the base class and this is called derieved class

class occupations(person):
    def __init__(self,name,age,occu):
        self.name=name
        self.age=age
        self.occu = occu

    def showDetails(self):
        print(f" Name :: {self.name}\n Age :: {self.age}\n Occupations :: {self.occu}")


b = occupations("Amit Pandey", 22,"Software engineer")
b.showDetails()
