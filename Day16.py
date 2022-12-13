# In this we will learn about match case which only works on python 3.10 and above
caseNo = int(input("Enter the case no: "))
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

match caseNo:
    case 1:
        print(num+num2)

    case 2:
        print(num-num2)

    case _:
        print("Default case")
