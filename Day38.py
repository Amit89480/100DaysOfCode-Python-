# in this we will be learning about raising the custom errors

# n = int(input("Enter the number between range"))
#
# if n < 5 or n > 10:
#     raise ValueError("Wrong range")

user = input("Enter the string:: ")


if user != "quit":
    raise ValueError("quiting the program")