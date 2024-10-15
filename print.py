###################################
## Some uses of print functions. ##
###################################

# print function with SEP.
regardMessage = "Hello, print"
nameMessage = "with SEP"
print("==== print function with SEP. ====")
print("Hello", "mi", "name", "is", "Python", sep=",")
print(regardMessage, nameMessage, sep="|")

# print function with END.
print("\n==== print function with END. ====")
helloMessage = "Hello, I'm a message"
endMessage = "with END"
print(helloMessage, end="|")
print(endMessage)

# print function with f-Strings.
print("\n==== print function with f-Strings. ====")
nameAutor = "Robin Sharma"
nameBook = "The 5 a.m club"
print(f"Autor: {nameAutor} - Book: {nameBook}")

# print function with format.
print("\n==== print function with format. ====")
nameSong = "Againts All Odds"
nameSinger = "Phil Collings"
stringResult = "Singer: {}, Song: {}".format(nameSinger, nameSong)
print(stringResult)

# print function with especific format.
print("\n==== print function with especific format. ====")
piValue = 3.14159
piValueFormat = "{:.2f}".format(piValue)
print("Vale of PI: ", piValueFormat)