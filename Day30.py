# In this we have learned about the recursion

# Factorial program

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


f = int(input("Enter the Number for factorial:: "))
ans1 = fact(f)
print(f"The factorial series of {f} is {ans1}")


# Fibonacci series

def fibonacci(n):
    if n == 0:
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the Number for fibonacci series:: "))
ans = fibonacci(n)
print(f"The fibonacci sequence of {n} is {ans}")
