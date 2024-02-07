#tuple
#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#ex2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#ex3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#ex4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#ex5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#ex6
tuple1 = ("abc", 34, True, 40, "male")
#ex7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#ex8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#ACCESS TUPLE
#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#ex2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#ex3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#ex4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#ex5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#ex6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#ex7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change values
#ex1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#ex2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#ex3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#ex4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#ex5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpacking
#ex1
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#ex2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#ex3
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

