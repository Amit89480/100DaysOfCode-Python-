# Exercise 2: Good morning sir wishes program


# time chart accordingly
# 4 to 12: Good Morning
# 12 to 16(4pm): Good evening
# 16 to 22(10pm):Good evening
# after 22 : Good Night
import time

CurrentHour = int(time.strftime('%H'))

if 4 <= CurrentHour < 12:
    print("Good Morning Sir")
elif 12 <= CurrentHour < 16:
    print("Good AfterNoon Sir!")
elif 16 <= CurrentHour < 22:
    print("Good Evening Sir!")
else:
    print("Good night Sir!")



