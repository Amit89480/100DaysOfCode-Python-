a = ["Amit","Ashis","Harry"]
 

#  Here we are using enumerete funtion to print the index with name

# for index,b in enumerate(a):
#         print(index,b)
#         if(index==1):
#             print("Yo man!")





# Here we are changing using the start=1 to change the index

for index,b in enumerate(a, start=1):
        print(index,b)
        if(index==1):
            print("Yo man!")
        