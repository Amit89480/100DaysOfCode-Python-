# In this we will be learning about the dict,dir and help method


# Below is for dir()
# x=[1,2,3]
# print(dir(x))





# Below is for __dict__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#
#
#
# P1=Person("Amit",21)
# print(P1.__dict__)



# Below is for help() method


print(help(Person))