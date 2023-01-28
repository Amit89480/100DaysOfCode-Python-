# In this we have learned about the access specifier


# Here we have demonstrated the public class

# class Myclass:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"Name is {self.name}")
#
# obj=Myclass("Amit")
# print(obj.name)


# Below we will be demonstrating the private class

# class Myclass:
#     def __init__(self,name):
#         # Putting the (__) will make it private
#         self.__name=name
#     def show(self):
#         print(f"Name is {self.name}")
#
# obj=Myclass("Amit")
#
# # for accessing the private member of a class
# print(obj._Myclass__name)


#  Below we will be learning about the protected

class Myclass:
    def __init__(self,name):
        self.name=name
    #     Here we did protected by just putting a single underscore->(_)
    def _show(self):
        print(f"Name is {self.name}")

# protected can be accessed within class or child class
class Myclass2(Myclass):
    pass


obj=Myclass2("Amit")
print(obj.name)