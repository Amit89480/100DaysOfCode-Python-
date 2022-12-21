# IN this we will be learning about the Tuple


# tuple created
tup1 = (4, 5, 6, 7)
print(tup1)


# Here by giving , it becomes tuple if we will not give it will become INT
tup2 = (1, )
print(type(tup2))


# positive slicing
print(tup1[1:3])



# negative slicing
print(tup1[:-2])



# using the In keyword to find out the whether the given element is presnt in tuple or not
if 5 in tup1:
    print("yes")

else:
    print("No")
