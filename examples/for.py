#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
for x in "banana":
  print(x)
#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ex5
for x in range(6):
  print(x)
#ex6
for x in range(2, 6):
  print(x)
#ex7
for x in range(2, 30, 3):
  print(x)
#ex8
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#ex9
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#ex10
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    