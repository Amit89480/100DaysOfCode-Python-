import os
if(os.path.exists("day")):
    print("NOt allowed")



# Here we have used rmdir to remove the file and we can use mkdir to make the file and for more info refer the docs


for i in range(0,100):
    os.rmdir(f"Day45/day{i+1}")


