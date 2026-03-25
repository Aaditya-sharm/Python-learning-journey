#Name and Age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old!")

#Two Numbers Operations
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
total = no1 + no2
difference = no1 - no2
product = no1 * no2
quotient = no1 / no2

print(total, difference, product, quotient)

#Average of 2 Int + 1 Float
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = float(input("Enter third number: "))

avg = (no1 + no2 + no3) / 3
print(avg, type(avg))

#Type Conversion Check
n = input("Enter your number: ")
a = int(n)
b = float(n)
c = str(n)
print(type(a), a)
print(type(b), b)
print(type(c), c)

#Temperature Conversion
temp = float(input("Enter temperature in Celsius: "))
farTemp = (temp * 9/5) + 32

print(farTemp)

#Integer & Decimal Part
num = float(input("Enter a decimal number: "))

int_part = int(num)
decimal_part = abs(num - int_part)

print("Integer part:", int_part)
print("Decimal part:", decimal_part)
