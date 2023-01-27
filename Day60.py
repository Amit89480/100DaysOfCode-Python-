# Here we are creating the class

class MyClass:
    def __init__(self, value):
        self.value = value


# Creating the constructor
    def show(self):
        print(f"Value is {self.value}")


    # setting up the getters
    @property
    def Getters(self):
        return self.value


    # Setting up the setters


    @Getters.setter
    def Setters(self, newvalue):
        self.value = newvalue


obj = MyClass(10)
obj.Setters= 45
print(obj.Setters)
obj.show()
