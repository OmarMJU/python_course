# Class 1: Introduction.
print("------- Class 1 -------")
print("It was only introduction!!")

# Class 2: Hello world.
print("\n------- Class 2 -------")
print("Hello, Omar!!!")
print(8+8)

# Class 3: Syntax and basic concepts.
print("\n------- Class 3 -------")
nameUser = "Omar"
print("Hi")
print(nameUser)

# Class 4: Class String.
print("\n------- Class 4 -------")
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
print("\n------- Class 5 -------")
x = 10
y = 5.5
print(type(x))
print(type(y))
print(x * y)

isTrue = True
isFalse = False

print(type(isTrue))
print(type(isFalse))

# Class 6: Input data.
print("\n------- Class 6 -------")
nameUser = input("Hi. Please type your name: ")
print(f"Hi, {nameUser}. Nice to meet you!!")
print("The data type is: ", type(nameUser))

ageUser = input("Now I need your age: ")
print(f"Wow, {ageUser} years old. That's great!!")
print("The data type is: ", type(ageUser))

ageUserInt = int(input("Please, give me your age one more time: "))
print(f"{ageUserInt} years old. No bad!!")
print("The data type is: ", type(ageUserInt))