#ex1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#ex2
x = Student("Mike", "Olsen")
x.printname()
#ex3
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
#ex4
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#ex5
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#ex6
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#ex7
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
#ex8
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)