# In this we will be learning about the dictionary

Dict = {89: "Amit", 78: "Misti", 80: "Ashis"}

# printing the dictionary

# print(Dict)
#
# print(Dict.keys())
#
# print(Dict.values())
#
#
# print(Dict[89])#->This will generate error if key value not found
# print(Dict.get(89))#-->this will give none if not found


# for keys in Dict.keys():
#     print(Dict[keys])


# print(Dict.items())


# If the values gets override


# Dict[89]="Ashsi122"
#
# Dict[90]="amit"

for keys,values in Dict.items():
    print(f"The accordingly keys {keys} and Value {values}")