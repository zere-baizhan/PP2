#ex1
def greeting(name):
  print("Hello, " + name)

#ex2
import mymodule

mymodule.greeting("Jonathan")


#ex3
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex4
import mymodule

a = mymodule.person1["age"]
print(a)

#ex5
import mymodule as mx

a = mx.person1["age"]
print(a)

#ex6
import platform

x = platform.system()
print(x)

#ex7
import platform

x = dir(platform)
print(x)

#ex8
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex9
from mymodule import person1

print (person1["age"])