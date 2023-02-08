class Employee:
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"the name of the employee is {self.name}")

    # We are writing this method to print the length of the name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name}"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("This is the Employee Class")
