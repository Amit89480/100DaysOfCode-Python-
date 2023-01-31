# In this we will be learning about the static method

class sm:
    def __init__(self, num):
        self.num = num

    def add(self, num):
        return self.num + num


    # This is a static method
    @staticmethod
    def addition(a, b):
        return a + b;


a = sm(8)
print(a.add(7))

# static method can be called directly without creating the instance
print(sm.addition(8, 9))
