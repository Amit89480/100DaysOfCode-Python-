# In this we have learned about f-string

# String format which was used earlier

a = "I am {} and I am from {}"
print(a.format("Amit","India"))


# Latest string formatting

name="Amit"
country = "india"
print(f"I am {name} and I am from {country}")


# use double brackets for excluding the f-string also called the string interpolation
print(f"I am {{name}} and I am from {{country}}")


# we can also print like this
#it is type of string
print(type (f"{2 * 30}"))
