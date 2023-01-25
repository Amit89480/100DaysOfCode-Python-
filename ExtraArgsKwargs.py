# In this we will be learning about the args and kwargs

# Below we are writting the args method
print("Below we have written the code for args...")

def namesList(*args):
    for item in args:
        print(item)

List=["amit","arjun","Misti","arnab"]
namesList(*List)


print("Below we have written the code for Kwargs...")

# Now we will be talking about the kwargs

def dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


list={"Amit":"Software Engineer","Misti":"Associate HR"}
dict(**list)