n=int(input("Enter the number of rows"))
num=1
row=1
while(row<=n):
    col=1
    while(col<=row):
        print(num,end=" ")
        num=num+1
        col=col+1

    print("\r")
    row=row+1


