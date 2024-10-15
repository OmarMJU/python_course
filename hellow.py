# Class 1: Introduction.
print("------- Class 1 -------")
print("It was only introduction!!")

# Class 2: Hello world.
print("------- Class 2 -------")
print("Hello, Omar!!!")
print(8+8)

# Class 3: Syntax and basic concepts.
print("------- Class 3 -------")
nameUser = "Omar"
print("Hi")
print(nameUser)

# Class 4: Class String.
print("------- Class 4 -------")
normalString = "Normal String"
print(">> \"", normalString, "\"", "is", type(normalString))

singleCuoteString = 'Single Cuote String'
print(">> \'", singleCuoteString, "\'", "is", type(singleCuoteString))

tripleCuoteString = '''Hi I'm 
a super pro
String
writed with Python...
In your fucking face Java!! Try me, bitch!!!
'''
print(">> \'''", tripleCuoteString, "\'''", "is", type(tripleCuoteString))

aSomeText = "Hello, Python!!"
print(">> The position -5 in the text", aSomeText, "is", aSomeText[-5])

firstString = "Smell"
secondString = "dog"
print(">>" + firstString + " " + secondString)
print(">>" + firstString * 3)

stringMethods = "The Class STRING has some Methods.     "
print(">> Lower case: " + stringMethods.lower())
print(">> Upper case: " + stringMethods.upper())
print(">> Strip case: " + stringMethods.strip())

# Class 5: Int, float, Bolean.
print("------- Class 5 -------")
x = 10
y = 5.5
print(type(x))
print(type(y))
print(x * y)

isTrue = True
isFalse = False

print(type(isTrue))
print(type(isFalse))