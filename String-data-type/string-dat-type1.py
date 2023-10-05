myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

#Working with Input Strings
name = input("What is your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print(name)
print(color)
print(animal)
print("{}, you like an {} {}!".format(name,color,animal))