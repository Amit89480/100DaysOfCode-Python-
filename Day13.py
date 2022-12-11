# In this we have learned about different string methods

a = "Amit"
print(a.upper())
print(a.lower())
b = "Amit is a good boy!!!!!!!!"
print(b.strip("!"))
print(b.replace("Amit", "Pandey"))

Split = "Amit is a good boy  !I am a good boy   we are good boys"
print(Split.split())

c = "Amit is a good boy"
print(c.capitalize())

print(c.center(50))

print(c.count("Amit"))

d = "Amit is a good boy ASAP"
print(d.endswith("ASAP"))
print(d.endswith("is", 4, 10))

print(d.find("a"))

print(d.index("a"))

checkALPHA = "Amit9989"
print(checkALPHA.isalnum())
print(checkALPHA.isalpha())

name = " Amit is a good boy\n"
print(name.islower())
print(name.isupper())

print(name.istitle())

space = "     "
print(space.isspace())


print(name.istitle())
print(name.isprintable())


test="amit is trying to learn python"
print(test.startswith("a"))


test2 = "Amit Is A good Programmer"
print(test2.swapcase())

print(name.title())
