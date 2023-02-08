#Python Classes/Objects
#Create a Class
class MyClass:
  x = 5 

#create object
p1=MyClass()
print(p1.x)


#__init__() Function
#Create a class named Person, use the __init__() function to assign values for name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#__str__() Function
#The string representation of an object WITHOUT the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


#The string representation of an object WITH the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



#Object Methods
#Insert a function that prints a greeting, and execute it on the p1 object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



#The self Parameter
#Use the words mysillyobject and abc instead of self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


#Modify Object Properties
#Set the age of p1 to 40
p1.age = 40
print(p1)

#Delete the age property from the p1 objec
del p1.age
print(p1)

#delete objects
del p1


#pass statement
class Person:
  pass



#*************EXERCISE****************
#Create a class named MyClass
class MyClass:
  x=5
c1=MyClass()
print(c1.x)