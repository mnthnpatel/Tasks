#python Inheritance
#Create a Parent Class
#Create a class named Person, with firstname and lastname properties, and a printname method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#Create a Child Class
#Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method
x = Student("Mike", "Olsen")
x.printname()

#Add the __init__() Function
#Add the __init__() function to the Student class
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc
    Person.__init__(self, fname, lname)

#Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


#Add Properties
#Add a property called graduationyear to the Student class
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add a year parameter, and pass the correct year when creating objects
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)


#methods
#Add a method called welcome to the Student class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)




#*************EXERCISE*******************
#What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?

