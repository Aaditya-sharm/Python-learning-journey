# Print Numbers from 1 to 10:
for i in range(1,11):
    print(i)

# Sum of first n numbers:
n=int(input("Enter your number: "))
total=0
for i in range(1,n+1):
    total+=i
print(total)

# Multiplication Table:
n=int(input("Enter your number: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# Count digits:
num = int(input("Enter your number: "))
if num == 0:
    count = 1
else:
    count = 0
    num = abs(num)    
    while num > 0:
        count += 1
        num //= 10
print(count)

# Print reverse of a number:
num = int(input("Enter your number: "))
rev_num = 0
sign = -1 if num < 0 else 1
num = abs(num)
while num > 0:
    one = num % 10
    rev_num = (rev_num * 10) + one
    num //= 10
print(sign * rev_num)

#Factorial of n:
n=int(input("Enter your number: ")) 
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)

#sum of digits of number:
num=int(input("Enter your number: "))
sum=0
if num == 0:
    sum = 0
else:
    num = abs(num)    
    while num > 0:
        sum=sum+num%10
        num //= 10
print(sum)

# Print pattern
n = int (input("Enter your number: "))
for i in range(1,n+1):
    print("*"*i)
    
# Reverse pattern
n = int (input("Enter your number: "))
for i in range(0,n+1):
    print("*"*(n-i))

# Number Reverse Pattern
n = int (input("Enter your number: "))
for i in range(n):
    for l in range(1,n-i+1):
        print(l,end="")
    print()
        
#Practice
n = int (input("Enter your number: "))
for i in range(1,n+1):
    for l in range(1,i+1):
        print(i,end="")
    print()

#Calculating final tax rate:
salary=int(input("Enter your salary: "))
F_tax_rate=0
if(salary<30000):
    F_tax_rate=salary*0.05
elif(salary<=70000):
    F_tax_rate=salary*0.15
else:
    F_tax_rate=salary*0.25
print(F_tax_rate)

#Program to print all numbers from 1 to 100 that are divisible by both 3 and 5:
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)

#Design a program to continuously input a number from user &print if it is positive or negative until the user enters “Quit”:
a=True
while(a==True):
    n=input("Enter your number: ")
    if n.lower() != "quit":
        n=int(n)
        if(n<0):
            print("The user entered negative number")
        else:
            print("The user entered positive number")
    else:
        a=False
        print("User Entered Quit")

#Palindrome Check 
num = int(input("Enter your number: "))
rev_num = 0
sign = -1 if num < 0 else 1
numb = abs(num)
while numb > 0:
    one = numb % 10
    rev_num = (rev_num * 10) + one
    numb //= 10
if abs(num)==rev_num:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")

#Print avg of 3 numbers
def avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg
avg(2,3,4)

#Sum of 2 numbers using lambda function
sum=lambda a,b:a+b
print(sum(4,5))

#print all even numbers
def even(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
    return 
even(2,10)

#Check prime number:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(4))
