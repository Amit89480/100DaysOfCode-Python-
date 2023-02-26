# In this we will be learning about the  Generator and yield function we use this suppose we are doing bigger
# calculation and we dont want to store larger list or value and also want perform higher calculation

def generator():
    for i in range(5):
        yield i


gen = generator()
print(next(gen))
print(next(gen))
