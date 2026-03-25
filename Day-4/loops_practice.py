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
