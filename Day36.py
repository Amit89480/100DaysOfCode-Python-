# In this we have learned about try and except

try:
    n=int(input("N = "))

    for i in range(1,11):
        print(f"{n} X {int(i)} = {int(n*i)}")
except ValueError:
    print("Invalid Input")

except IndexError:
    print("Indention Error")

print("We are done with the program")