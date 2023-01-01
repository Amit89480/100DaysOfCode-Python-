# In this we have learned about how to use else with for and while loop


# Code to use else with for loop

# for i in range(1, 6):
#     print(i)
#
#
# else:
#     print("Out of Scope")


# here the code will not work as we are using break

for i in range(9):
    print(i)
    if i == 4:
        break

else:
    print("Out of Scope")

print("Loop Completed")
