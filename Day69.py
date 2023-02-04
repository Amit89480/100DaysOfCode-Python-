class employee:
    company = "Apple"

    def showDetails(self):
        print(f"The employee name is {self.name} and the company name is {self.company}")
    # we are using this decorator to modify the class name
    @classmethod
    def changeClassVariableName(cls, newCompanyName):
        cls.company = newCompanyName


E1 = employee()
E1.name="Amit"

E1.showDetails()
# Here it will modify the class variable name
E1.changeClassVariableName("Tesla")
E1.showDetails()

print(employee.company)