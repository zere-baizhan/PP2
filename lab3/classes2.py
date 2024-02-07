#ex1
"""class getString():
    def __init__(self):
        self.string=input()
class printString():
    def __init__(self,string):
        self.string=string.upper()
        print(self.string)

string_input=getString()
print_string=printString(string_input.string)"""

#ex2
"""class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
    def area(self):
        return self.length **2

shape=Shape()
print(shape.area())
x=int(input())
square=Square(x)
print(square.area())"""

#ex3
"""class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
    def area(self):
        return (self.length*self.width)

shape=Shape()
print(shape.area())
x=int(input())
y=int(input())
rectangle=Rectangle(x,y)
print(rectangle.area())"""

#ex4
"""import math
class Point:
    
    def __init__(self,x,y,):
        self.x=x
        self.y=y
    
    def Show(self):
        print("cordinates are: ",self.x,self.y)
    
    def Move(self,x1,y1):
        self.x=x1
        self.y=y1
    
    def Distance(self,other):
        distance=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        distance=math.ceil(distance)
        return distance

#initializing the coodrinates and passing it to the parametr   
x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
p1=Point(x1,y1)
p2=Point(x2,y2)

#show the co-s
p1.Show()
p2.Show()

#moving
p1.Move(2,3)
#show it
p1.Show()

#distance
distance=p1.Distance(p2)
print("the distance is", distance)"""

#ex5
class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    #putting money to the depo
    def Deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(name+",you entered",amount,"dollars")
        else:
            print("unavailable!")
        
    def Withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(name+",you withdraw",amount,"dollars from your deposit")
            else:
                print(name+",you dont have that much money to withdraw")
        else:
            print(name+",you should take more money than 0")

name=input()
amount=int(input())
account=Account(name,amount)

account.Deposit(500)
account.Withdraw(200)
account.Withdraw(1500)
account.Withdraw(0)

print(name+" now you have: ",account.balance)