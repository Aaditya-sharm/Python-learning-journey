from abc import ABC,abstractmethod

#Create a BankAccount class with attributes account_number owner_name and balance.Add methods to deposit withdraw and check balance
class BankAccount:
    def __init__(self, acc_no, owner_name, balance):
        self.acc_no = acc_no
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def get_balance(self):
        print(f"Your balance is {self.balance}")

acc1 = BankAccount("2374239487", "Aaditya", 1000)

acc1.get_balance()

acc1.deposit(500)
acc1.get_balance()

acc1.withdraw(300)
acc1.get_balance()

#Create a class Book with the following attributes: •title •author •list of reviews And add methods to : •add a new review •count reviews •display all reviews
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=[]

    def add_review(self,review):
        self.reviews.append(review)
    def count_review(self):
        return len(self.reviews)
    def display_reviews(self):
        if not self.reviews:
            print("No reviews available")
        else:
            print(f"Reviews for '{self.title}' by '{self.author}':")
            for i , reviews in enumerate(self.reviews, start=1):
                print(f"{i}. {reviews}")
        
Book1=Book("Harry Potter","JK Rowlin")
Book1.add_review("This book was really amazing")
Book1.add_review("Best book i ever read")
Book1.count_review()
Book1.display_reviews()

#Create a class Student with private attributes _name, _roll_no,and_marks.Provide getter and setter methods with validation(e.g.,marks cannot be negative,roll number has to be between 1&100 & name cannot be empty)
class Student:
    def __init__(self,name,roll_no,marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
        
    def get_marks(self):
        return self.__marks
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def set_marks(self,marks):
        if marks>=0:
            self.__marks=marks
        else:
            print("Marks cannot be negative.")
    def set_name(self,name):
        if name.strip()=="":
            print("Name cannot be empty")
        else:
            self.__name=name
    def set_roll_no(self,roll_no):
        if roll_no<=100 and roll_no>0:
            self.__roll_no=roll_no
        else:
            print("Roll_no should be between 1 to 100")    
stu1=Student("aadi",1,100)
print(stu1.get_marks())
print(stu1.get_name())
print(stu1.get_roll_no())
stu1.set_marks(99)
print(stu1.get_marks())
stu1.set_name("Aaditya")
print(stu1.get_name())

    
# Create a class Shape with method area(). Create sub classes Circle,Rectangle and Triangle that override the area() method.

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area (self):
        print(f"Area of rectangle is {self.l*self.b}")
class Circle(Shape):
    def __init__(self,rad):
        self.rad=rad
        self.pi=3.14
    def area(self):
        print(f"Area of circle is {self.pi*self.rad**2} ") 

class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base
    def area(self):
        print(f"Area of Triangle is {0.5 * self.base * self.height}")
rec1=Rectangle(3,10)
rec1.area()

# Create a base class Vehicle with some attributes.Create 2 subclass that add extra attributes.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand 
        self.model=model
class Car(Vehicle):
    def __init__(self,seats,brand,model):
        super().__init__(brand,model)
        self.seats=seats
class Bike(Vehicle):
    def __init__(self,engine_cc,brand,model):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

car1=Car(6,"ROlls Royalce",1987)
print(car1.model)

# Create an abstract class Employee with an abstract method calculate_salary().Create subclass intern,fulltimeemployee and contractbasedEmployee that implement the method differently
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
    def __init__(self,stipend):
        self.stipend=stipend
    def calculate_salary(self):
        return self.stipend
class FullTimeEmployee(Employee):
    def __init__(self,base,bonus):
        self.base=base
        self.bonus=bonus
        self.salary=base+bonus
    def calculate_salary(self):
        return self.salary
class Contract(Employee):
    def __init__(self,hourly_rate,hrs):
        self.hourly_rate=hourly_rate
        self.hrs=hrs
        self.salary=hourly_rate*hrs
    def calculate_salary(self):
        return self.salary
employees = [
    Intern(10000),
    FullTimeEmployee(50000, 10000),
    Contract(500, 20)
]

for emp in employees:
    print(emp.calculate_salary())
        
#Create a class Person that allows the constructor to work with: •name only •name+age •name+ age + address As direct constructor overloading (multiple constructors)are not allowed but we have to use default parameters to simulate constructor overloading.
class Person:
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(f"Name: {self.name}")
        if self.age is not None:
            print(f"age: {self.age}")
        if self.address is not None:
            print(f"Address is {self.address}")

p1 = Person("Aadi")
p2 = Person("Aadi",19)
p3 = Person("Aadi",19,"2338 sec-15 Sonipat")

p1.display() 
p2.display()
p3.display()

# Create a class player with 1)a class variable player_count 2)instance variables name and level. Track how many players were created.
class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1
    @classmethod
    def get_total_playerCount(cls):
        print(f"Total player count is {cls.player_count}")

p1=Player("Aaditya",99)
p2=Player("CyberAadi",100)
Player.get_total_playerCount()

# Create following classes Herbivores,Carnivores,Omnivores with some attributes and methods.Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance work:

class Herbivores:
    def __init__(self):
        print("I only eat plants")
        super().__init__()
class Carnivores:
    def __init__(self):
        print("I only eat flesh")
        super().__init__()
class Omnivores:
    def __init__(self):
        print("I eat both plants and animals.")
class Bear(Herbivores,Carnivores,Omnivores):
    def __init__(self):
        super().__init__()
bhalu=Bear()
class Employee:
    start_time="9:00am"
    end_time="6:00pm"

    def new_time(self,new):
        self.end_time=new
    
class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject

t1=Teacher("Maths")
t1.new_time("8:00pm")
print(t1.subject,t1.start_time,t1.end_time)
#instance method:
class student:
    subject="Python"
    college="Ram lal"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def get_info(self):
        print(f"The student's name is {self.name} and roll no is {self.roll_no}")

stu1=student("Aaditya",1)
stu2=student("Abhi",2)

stu1.get_info()
stu2.get_info()


#class method and static method:

class Laptop:
    storage_type="ssd"

    def __init__(self,ram,company):
        self.ram=ram
        self.company=company

    @classmethod
    def get_storage_type(cls):
        print(f"The storage type of laptop is {cls.storage_type}")

    @staticmethod
    def discounted_price(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price is {final_price}")


L1=Laptop("16gb","Asus")
L2=Laptop("8GB", "Dell")

L1.get_storage_type()
L1.discounted_price(40000,10)

# Design and create an online store for products(name,price).Track total products being created. Create a static method to calculate discount on each product based on % parameter

class Products:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Products.count += 1

    def get_info(self):
        print(f"The product is {self.name} and its price is Rs.{self.price}.")

    @classmethod
    def get_total_products(cls):
        print(f"The total products stored = {cls.count}")


    @staticmethod
    def discounted_price(price,discount):
        final_price=price-(discount*price/100)
        print(f"The final price of the product will be {final_price}.")
        
product1=Products("Shampoo",500)
product2=Products("IPhone",50000)
product3=Products("Camera",30000)
product4=Products("Laptop",90000)

product2.get_info()
product4.get_info()

product4.discounted_price(product4.price,10)
product1.discounted_price(product1.price,16) 

Products.get_total_products()
 

