
n1=int(input("Enter your number"))
n2=int(input("Enter your number"))
n3=int(input("Enter your number"))

if(n1>=n2 and n1>=n3):
    print(f"{n1} is largest")
elif(n2>=n1 and n2>=n3):
    print(f"{n2} is largest")
else:
    print(f"{n3} is largest")
