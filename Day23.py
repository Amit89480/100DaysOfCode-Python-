# In this we will be learning about the concepts of List methods
list = [1, 5, 6, 3, 2, 9, 8, 6, 7]

print(list)
list.sort()
print(list)

list.sort(reverse=True)
print(list)

print(list.index(1))

print(list.count(6))

# m= list
# m[0]=34
# print(m)
# print(list)


copyList = list.copy()
print(copyList)

list.insert(1, 100)
print(list)

list.extend(copyList)
print(list)

l = [9, 6, 4, 6, 4, 4, 6, 4]
m = [3, 6, 79, 6, 4, 6, 4, 4, 6, 4]
k = l + m
print(k)
