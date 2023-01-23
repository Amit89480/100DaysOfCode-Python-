class person:
    name = "Amit"
    Age = 90
    # self keyword is used to accesed the instance of the particular class
    def info(self):
        print(f"{self.name} is {self.Age} years old")


Amit = person()
Amit.name="Misti"
Amit.info()
