# Even Odd checker
no=int(input("Enter your number: "))
if(no%2==0):
    print(f"Number {no} is even")
else:
    print(f"Number {no} is odd")

# Largest of 3 numbers
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))
if(num1>=num2 and num1>=num3):
    print(f"{num1} is greatest")
elif(num2>=num1 and num2>=num3):
    print(f"{num2} is greatest")
elif(num3>=num1 and num3>=num2):
    print(f"{num3} is greatest")


#Voting Eligibility
age=int(input("Enter your age: "))
if(age>=18):
    print("Candidate is eligible to vote.")
else:
    print("Candidate is not eligibile to vote.")

# Number Sign Checker
num=int(input("Enter your number: "))
if(num>0):
    print(f"Number is positive")
elif(num<0):
    print(f"Number is negative")
else:
    print("Number is zero")

# Grade System
marks=int(input("Enter students marks: "))
if(marks>=90):
    print("Student got A grade")
elif(marks>=75):
    print("Student got B grade")
elif(marks>=50 ):
    print("Student got C grade")
else:
    print("Student is fail")

# Take 3 numbers → print smallest number
numb1=int(input("Enter your first number: "))
numb2=int(input("Enter your second number: "))
numb3=int(input("Enter your third number: "))
if(numb1<=numb2 and numb1<=numb3):
    print(f"{numb1} is smallest")
elif(numb2<=numb1 and numb2<=numb3):
    print(f"{numb2} is smallest")
elif(numb3<=numb1 and numb3<=numb2):
    print(f"{numb3} is smallest")

