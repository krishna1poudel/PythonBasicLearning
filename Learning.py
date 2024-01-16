#looping through a string

y="helloworld"

for x in y:
    print(x)

#for the string length we use len(variable)
print(len(y))


#Slicing in python

b="hello, world"
print(b[2:5])
# this output is llo.



from os import name
import random
# for the random variable we import random (start and stop define the starting and stoping of the function)
print(random.randrange(start=1,stop=10))

#upppercase and lowercase change string

f="hello, wOrld  "
print(f.upper())

print(f.lower())

#for the remove  whitespace in the string

print(f.strip())

#User replace in python

print(f.replace("h","i"))

#String concatenation in Python
a="hello"
b="world"
c=a+b
print(c)
f=9
print("my name is krihna",9) # any number and string join together by , sign in print

#format() in python

age=24
txt="my name is krishna poudel, and i am {}"
print(txt.format(age)) 
# here format is use to give the age i.e insert number into string
 
    #using mutlple value i.e
quantity=3
itemno=567
price=49.95
myorder="I want {} pieces of item{} for {}dollars."
print(myorder.format(quantity,itemno,price))


#String methods
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


#normal function try yourself
#lamba function take  multiple argument yourself

# this is my first class 
class  firstclass:
    x=5

pl=firstclass()

print(pl.x)


#Here i use   __init__()  All the classes have __init__() this function which is always executed when the class is beign initiated.
# so intially it is used to initaled the parameter inside
class krishna:
    def __init__(self , age, name):
        self.age=age
        self.name=name
        
p1=krishna(15,"krishna poudel dai")

print(p1.name)

#inheritance in phyton.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
    
x=Student("krishna","poudel",2012)
x.welcome()



#iterator Technically, in Python, an iterator is an object which implements 
# the iterator protocol, which consist of the methods __iter__() and __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#iter with polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  
  # try yoursely scope of the varible i.e local and global
  
  #Python Modules in module different file in same folder Python.
  
  
  
  

  
  
  


