
#Ask the user for a string and check whether it is a palindrome or not.
name=input("Enter your name: ")
rev_name=name[::-1]
if(name==rev_name):
    print(f"{name} is palindrome")
else:
    print(f"{name} is not a palindrome")
    
# Write a program that takes a string from the user and prints the number of spaces in the string:
para=input("Enter your paragraph: ")
print(para.count(" "))

# Ask the user for a string and print :•All unique characters •The count of unique characters
user = input("Enter your string: ")
uniq = ""
for ch in user:
    if ch not in uniq:
        uniq += ch
print("Unique characters:", uniq)
print("Count:", len(uniq))
#using loops with lists
nums=[1,2,3,10,4] 
x=10
idx=0
for value in nums:
    if value==x:
        print(f"x found at idx={idx}")
        break
    idx+=1

#adding values of tuple
tup=(1,2,3,4)
al=0
for val in tup:
    al+=val
print(al)

#list all unique course
info=[
    ("Aadi","English"),
    ("Aakash","Hindi"),
    ("Suraj","Skt"),
    ("Chanda","Maths"),
    ("Bhagwati","Hindi")
    ]
uni=set()
for tup in info:
    uni.add(tup[1])
print(uni)

#list students enrolled in english
infor=[
    ("Aadi","English"),
    ("Aakash","Hindi"),
    ("Suraj","Skt"),
    ("Chanda","Maths"),
    ("Bhagwati","English")
    ]
for name,course in infor:
    if(course=="English"):
        print(name)

# Given a list of integers compute the average of all numbers in the list.
l1=[1,2,3,4,5,10,7]
print(sum(l1)/len(l1))

# Input two lists of integers from the user. Merge them in to one list and sort the result .
l2=list(map(int,input("Enter your numbers: ").split()))
l3=list(map(int,input("Enter your numbers: ").split()))
merg_li=l2+l3
merg_li.sort()
print(f"The merged list is {merg_li}")

# Create tuple of all 1) odd numbers and 2) even numbers:
inte=(1,2,3,4,5,6,7,8,9,10)
odd_tup=()
even_tup=()
for i in inte:
    if i%2==0:
        i=(i,)
        even_tup+=i
    else:
        i=(i,)
        odd_tup+=i
print(f"odd_tup is {odd_tup} and even_tup is {even_tup}")


# Write a program to check whether two lists share no common elements.
l1=[1,2,3,4]
l2=[5,6,2,7,8,9,10]
s1=set()
s2=set()
for i in l1:
    s1.add(i)
for i in l2:
    s2.add(i)
if s1 & s2:
    print(f"These lists share common elements which are {s1.intersection(s2)}")
else:
    print("These share no common elements")

# Given a list , print all elements that appear more than once in the list.
lis=[1,2,3,4,5,6,7,2,9,4,10]
seen = set()
duplicates = set()
for i in lis:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)
# Create a dictionary where: •Keys=student names •Values=marks(integer) Write a menu-based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary: 1.A-Add a student 2.B-Update marks 3.C-Search for a student 4.D-Display all students and marks:
stu_det = {
    "Aaditya": 90,
    "Bhai": 80,
    "Papa": 97,
    "Mummy": 99,
    "Bags": 88
}
while True:
    command = input("A:Add B:Update C:Search D:Display E:Exit → ").upper()
    if command == "A":
        stu = input("Enter student name: ").title()
        marks = int(input("Enter marks: "))
        stu_det[stu] = marks

    elif command == "B":
        stu = input("Enter student name: ").title()
        if stu in stu_det:
            marks = int(input("Enter new marks: "))
            stu_det[stu] = marks
        else:
            print("Student not found")

    elif command == "C":
        stu = input("Enter student name: ").title()
        if stu in stu_det:
            print(f"{stu}: {stu_det[stu]}")
        else:
            print("Student not found")

    elif command == "D":
        for name, marks in stu_det.items():
            print(name, ":", marks)

    elif command == "E":
        print("Exiting program")
        break

    else:
        print("Invalid choice")

# Create a dict that maps each word of list to its length:
words =["apple","banana","kiwi","cherry","mango"]
word_len={}
for i in words:
    word_len.update({i:len(i)})
print(word_len)

#Create dictonary using values given in list of tuples
inform=[
    ("Aadi","English"),
    ("Aakash","Hindi"),
    ("Suraj","Skt"),
    ("Chanda","Maths"),
    ("Bhagwati","English")
]
student_dict={}
for t in inform:
    student_dict.update({t[0]:t[1]})
print(student_dict)
