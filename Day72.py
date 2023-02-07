# In this we will be learning about the super keyword


class parents:
    def __init__(self,name,age):
        self.name=name
        self.age=age


# Here we are inherting and accessing the parents methods using the super keyword
class child(parents):
    def __init__(self,name,age,lang):
        super().__init__(name,age)
        self.lang=lang

e1=child("Amit",23,"C++")
print(e1.lang)
e2=parents("Amit",45)
print(e2.name)


