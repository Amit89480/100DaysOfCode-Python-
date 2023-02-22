# In this we will be learning about the Shutil module


import shutil
import os

shutil.copy("Day87.py","Daytest.py")
os.remove("Daytest.py")

# Like this there are many methods like rmtree,copy2