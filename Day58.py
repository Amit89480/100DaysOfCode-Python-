class Person:
    def __init__(self):
        print("I am default constructor")

    def __init__(self, name, occu):
        self.name = name
        self.occu = occu
        print("I am class Person")

    def info(self):
        print(f"{self.name } is a {self.occu}")


a = Person("Amit","Developer")
b = Person("Misti", "HR")
print(a.info())
print(b.info())
