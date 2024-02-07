#lists
#ex1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#ex4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#ex5
list1 = ["abc", 34, True, 40, "male"]
#ex6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#ex7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#ACCESS
#ex1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#ex2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#ex3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#ex4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#ex6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#ex7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#CHANGE
#ex1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#ex4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#ex5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#APPEND
#ex1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#ex4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#REMOVE
#ex1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#ex4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#ex5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#ex6
thislist = ["apple", "banana", "cherry"]
del thislist
#ex7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#