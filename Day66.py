# In this we will be learning about the class and the instance variable

class Employee:
    # Below we have created the class variable
    companyName="Apple"
    noofEmployee=0
    # Below we are creating the instance variable
    def __init__(self,name):
        self.name=name
        Employee.noofEmployee += 1;
    def showDetails(self):
        print(f"The name of the employee in {self.noofEmployee} sized company is {self.name}")



emp1=Employee("Amit")
emp1.showDetails()

emp2=Employee("Misti")
emp2.showDetails()