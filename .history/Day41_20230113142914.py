a = ["Amit","Ashis","Harry"]
 

#  Here we are using enumerete funtion to print the index with name

# for index,b in enumerate(a):
#         print(index,b)
#         if(index==1):
#             print("Yo man!")







for index,b in enumerate(a, start=1):
        print(index,b)
        if(index==1):
            print("Yo man!")
        