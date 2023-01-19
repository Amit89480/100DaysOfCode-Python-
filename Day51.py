#Here we will be learning about the seek(), tell() and truncate()

# with open('myfile','r')as f:
#     f.seek(10)
#     data=f.read(5)
#     print(data)

# with open('myfile','w')as f:
#     f.seek(10)
#     print(f.tell())



# Here we have used truncate
with open('myfile','w')as f:
    f.write("Hello world")
    f.truncate(5)
with open('myfile','r')as f:
    print(f.read())