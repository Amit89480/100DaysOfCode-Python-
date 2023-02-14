# In this we will be learning about the multiple inheritance in python


class employee:
    def __init__(self,name):
        self.name=name

class Language:
    def __init__(self,language):
        self.language=language



class Rate(employee,Language):
   def __init__(self,language,name,rating):
       self.name=name
       self.language=language
       self.rating=rating







# Here MRO stands for method resolution order

emp1= Rate("Amit","C++",9)
print(emp1.rating)
print(Rate.mro())