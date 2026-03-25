
#Length + First + Last Character
name = input("Enter your name: ")
if len(name) > 0:
    print("Length:", len(name))
    print("First character:", name[0])
    print("Last character:", name[-1])
else:
    print("Empty string entered")

#Reverse String
name= input("Enter your name: ")
print("Reversed:", name[::-1])

#Concatenation
str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)

#
