# In this we will be learning about the file handaling


# Here we are reading the file content
f = open('myfile', 'r')
text = f.read()
print(text)
f.close()



# Here we are writting inside the file content
f=open('myfile','w')
f.write("Hey I am getting Modified")
f.close()

# The with statement to automatically close the file
with open('myfile','w') as f:
    f.write("Hey I am again getting modified!!")


# Here we are creating a new text file
with open('myfile2','x') as f:
    text=f.read()
    print(text)
