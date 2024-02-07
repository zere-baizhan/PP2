#ex1
"""def grams2ounces(n):
    ounces=28.3495231 * n
    return ounces

n=int(input())
print(grams2ounces(n))"""

#ex2
"""def farenheit2celcium(F):
    C= (5/9) * (F - 32)
    return C
F=int(input())
print(farenheit2celcium(F))"""

#ex3
"""def solve(numheads,numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    return rabbit,chicken

numheads=int(input())
numlegs=int(input())
print(solve(numheads,numlegs))"""

#ex6
"""def reversentence(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    reversed_sentence=' '.join(reversed_words)
    return reversed_sentence

input=input()
reversed_sentence=reversentence(input)
print(reversed_sentence)"""

#ex7
"""def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

numbers = input()
numslist = list(map(int,numbers.split()))
print(has_33(numslist))"""

#ex8
"""def spy_game(nums):
    found_0 = False
    found_00 = False

    for num in nums:
        if num == 0:
            if not found_0:
                found_0 = True
            elif found_0 and not found_00:
                found_00 = True
        elif num == 7 and found_00:
            return True
    return False

numbers = input()
numslist = list(map(int,numbers.split()))
print(spy_game(numslist))"""

#ex9
"""def volumeofsphere(radius):
    v=(4/3)*3.14*(r**3)
    return v
r=int(input())
print(volumeofsphere(r))"""

#ex10
"""def unique_elements(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list
numbers = input()
numslist = list(map(int,numbers.split()))
print(unique_elements(numslist))"""

#ex11
"""def is_Palindrome(string):
    reversed_string=string[::-1]
    if string==reversed_string:
        return True
    return False
string=input()
print(is_Palindrome(string))"""

#ex12
"""def histogram(numbers):
    for i in numbers:
        print('*' * i)
numbers = input()
numslist = list(map(int,numbers.split()))
print(histogram(numslist))"""

#ex13
import random
def Guess_the_number(name):
    
    secret_number = random.randint(1, 20)
    cnt=0
    
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess :)")
    
    while True:
        guess=int(input())
        cnt+=1
        if guess == secret_number:
            print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

name = input("Hello! What is your name? ")

Guess_the_number(name)   


