#ex1
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#ex2
txt = "The price is {:.2f} dollars"

#ex3
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))