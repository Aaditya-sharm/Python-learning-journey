# Check does python word exist in sample.txt if yes then on which line number
data=True
line=1
with open ("sample.txt","r") as f:
    while data:
        data = f.readline()
        if "Python" in data:
            print(f"Word found at line {line}")
            break
        print(data)
        line+=1
import json

py_val={
    "Name":"AAditya",
    "class":"Bteach 2nd pear",
    "Roll_no":1
}
# square of elements in list:
li=[1,2,3,4,5,6]
li=[ i*i for i in li ]
print(li)

# square of odd elements in list:
li=[1,2,3,4,5,6]
li=[ i*i for i in li if i%2!=0]
print(li)

# print 0 if value is -ve or print the same number:
li=[-10,4,-2,3,32,10,-1]
li=[0 if val<0 else val for val in li]
print(li)

#convert all names of list into UpperCase:
name=["aaditya","romeo","juliet","sham","Andrew"]
name=[val.upper() for val in name]
print(name)
import json
# Create a program that Opens a file in write mode names.txt a) Writes 5 names (one per line) entered by the user b)Then opens the same file in read mode and prints all names.
with open ("names.txt","w") as f:
    for i in range(5):
        name=input("Enter your name: ")
        f.write(name + "\n")
with open("names.txt","r") as f1:
    name=f1.read()
    print(name)

# Create a program that: 1.Opens a file in append mode "log.txt" 2.Adds a new log entry(like"Program run successfully")3.Opens the file in read mode and prints all logs
with open ("log.txt","a+") as f2:
    f2.write("Program run successfully \n")
with open ("log.txt","r") as f:
    logs=f.read()
    print(logs)

# Create a program that: 1. Has a list of numbers: [5, 10, 15, 20, 25] 2.Uses a list comprehension to create a new list with only numbers greater than 15 Print the new list
l1=[5, 10, 15, 20, 25]
l2=[i for i in l1 if i>15]
print(l2)

# Create a Python dictionary of 3 cities and their populations. Save it to "cities.json" 1.Then load the JSON and print each city and its population. 2. Ask the user for a new city &its population - update this info in the json file
City ={
    "Sonipat":1000,
    "Rohtak":900,
    "Jind":500
}
with open ("cities.json","w") as f:
    json.dump(City,f,indent=4)
with open("cities.json","r")as f:
    Data=json.load(f)
    for city,popul in Data.items():
        print(f"{city}:{popul}")
    city_name=input("Enter your city name: ")
    population=int(input("Enter its population: "))
    Data[city_name] = population
with open("cities.json","w") as r:
    json.dump(Data,r,indent=4)

# Write a program that tries to open "data.txt" in read mode.If the file does not exist ,catch the exception and print "File not found!".
try:
    with open("data.txt","r") as r:
        a=r.read()
        print(a)
except FileNotFoundError:
    print("File not found!")
