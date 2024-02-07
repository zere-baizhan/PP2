#ex1
a = "Hello"
print(a)
#ex2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#ex3
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#ex4
a = "Hello, World!"
print(a[1])
#ex5
for x in "banana":
  print(x)
#ex6
a = "Hello, World!"
print(len(a))

#ex7
txt = "The best things in life are free!"
print("free" in txt)
#ex8
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#ex9
  txt = "The best things in life are free!"
print("expensive" not in txt)
#ex10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#SLICING strings

#ex1
b = "Hello, World!"
print(b[2:5])
#ex2
b = "Hello, World!"
print(b[:5])
#ex3
b = "Hello, World!"
print(b[2:])
#ex4
b = "Hello, World!"
print(b[-5:-2])

#MODIFY
#ex1
a = "Hello, World!"
print(a.upper())
#ex2
a = "Hello, World!"
print(a.lower())
#ex3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#ex4
a = "Hello, World!"
print(a.replace("H", "J"))
#ex5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenation

#ex1
a = "Hello"
b = "World"
c = a + b
print(c)
#ex2
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#FORMAT
#ex1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#ex2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#ex3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#escape characters
#ex1
txt = "We are the so-called \"Vikings\" from the north."

