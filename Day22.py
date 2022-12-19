# In this we will learn about List and List Comprehension

# Here we have created the List
list = ["amit", "ashis", "misti"]
print(list)
print(list[0])
print(list[1])
print(list[2])


# Negative Indexing
print(list[:-1])


# Searching for element in List
if "amit" in list:
    print("yes")
else:
    print("no")


# Here we are performing the JumpIndex
print(list[0:len(list):2])


# Here we are searching for a group of character in a String
if "mit" in "Amit":
    print("yes")
else:
    print("NO")

# List Comprehension
# Creating for List from an iterable object

list1 = [i for i in range(10) if i % 2 == 0]
# Here by using list comprehension we are creating another list
list2 = [i for i in list]
print(list1)
print(list2)
