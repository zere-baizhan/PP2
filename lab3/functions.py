#ex1
def my_function():
    print("Hello from a function")

#ex2
def my_function():
  print("Hello from a function")
my_function()

#ex3
def my_function(fname, lname):
  print(fname)

#ex4
def my_function(x):
     return x+5

#ex5
def my_function(*kids): # * number of arguments are unknown
  print("The youngest child is " + kids[2])

#ex6
def my_function(**kid): # ** unknown number of keywords
  print("His last name is " + kid["lname"])