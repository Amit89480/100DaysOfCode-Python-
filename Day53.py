# In this we will be learning about the map,filter and reduce


from functools import reduce
# Here is Map
# def cube(x):
#     return x*x*x
#
#
l=[6,7,8,4,3]

# newList=list(map(cube,l))
# print(newList)

# Will print this -> [216, 343, 512, 64, 27]


# Here we will be doing about the filter

# newL=list(filter(lambda x:x>6,l))
# print(newL)


# Here we will be talking about the Reduce

newL1=reduce(lambda x,y:x+y,l)
print(newL1)



