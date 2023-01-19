# In this we will be learning about the global and the local variable

x = 10

print(f"The global here is {x}")

def func():
    global x
    x=20
    print(f"In the function we have modify the global varibale using global keyword -> {x}")

func()
