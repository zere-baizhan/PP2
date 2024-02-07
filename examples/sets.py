#SETS
#ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#ex2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#ex3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#ex4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#ex5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#ex6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#ex7
set1 = {"abc", 34, True, 40, "male"}

#ex8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#ex9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#ACCESS
#ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#ex2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ADD ITEMS
#ex1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#ex2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#ex3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#REMOVE
#ex1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#ex2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#ex3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#ex4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
