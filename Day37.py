# In this we will be learning about the Finally keyword

# let say we have created a simple program
#
# try:
#     list = [7,8,9,4,5]
#     i = int(input("Enter the index to print"))
#     print(list[i])
# except ValueError:
#     print("Invalid Syntax")
#
# finally:
#     print("I will always execute")




def funct1():
    try:
        list = [7, 8, 9, 4, 5]
        i = int(input("Enter the index to print:: "))
        print(list[i])
        return 1
    except ValueError:
        print("Invalid Syntax")
        return 0
# here finally will execute no matter whether function return or not ot is used to revoke database to break the cponnection
    finally:
        print("I will always execute")


x=funct1()
print(x)

