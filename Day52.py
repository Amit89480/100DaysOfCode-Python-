# In this we will be learning about the lambda functions

def ftof(func,value):
    return 6+func(value)




double = lambda x:x*x*x


print(double(6))
# Here we are passing a function to function
print(ftof(lambda x:x*x,6))