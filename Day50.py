# In this we will be learning about the readLines and writeline method


# Here we are using readLine to readLine including new lines
f= open('myfile','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# Here we will be using Writeline

f=open('myfile','w')
lines=['line1\n','line2\n','line3\n']

f.writelines(lines)
f.close()
