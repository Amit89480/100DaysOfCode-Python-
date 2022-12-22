# In this we have learned about the Tuple method


# Here to change anything in tuple first convert it into list and then change
tuple1 = ("Ashis","Misti","Payel","Misti")

temp= list(tuple1)
temp.pop(2)

temp[2]="Misti"

print(temp)

tuple1=tuple(temp)

print(tuple1)


# Methods in tuple
tuple2 = (4,5,6,2,2,2,2,3,5,6)
res1=tuple1.count("Ashis")
print(res1)
# .index have three arguments element , start, end
res=tuple2.index(2,3,7)
print(res)

