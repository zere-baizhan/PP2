#ex1
"""def calculate_factorial(n):
    if n == 0: 
        return 1 

    return n*calculate_factorial(n-1)
num=int(input())
print(calculate_factorial(num))"""

#ex2
"""def reverse_string(str):
  return str[::-1]
s=input()
print(reverse_string(s))"""

#ex3
"""def get_max(a,b,c):
    return(max(a,b,c))
a,b,c=map(int, input().split())
print(get_max(a,b,c))"""

#ex4
"""def is_even(n):
    if(n%2==0):
        return True
    else:
        return False

n=int(input())
print(is_even(n))"""

#ex5
#check if its prime
"""def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
#filtering in
def filter_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            primes.append(num)
    return primes

#entering the nums
numbers = input()
#splitting it
numslist = list(map(int,numbers.split()))
#initialize
primes = filter_prime(numslist)

print(primes)"""

#ex6
"""def find_common_elements(ls1,ls2):
    cnt=0
    commons=[]
    for i in ls1:
        for j in ls2:
            if i==j:
                commons.append(i)
                cnt=cnt+1
    return commons,cnt

n1=input()
n2=input()

#splitting it
num1 = list(map(int,n1.split()))
num2 = list(map(int,n2.split()))
#initialize
common,cnt = find_common_elements(num1,num2)
if cnt>0:
    print(common)
else:
    print("no common elements")"""

#ex7
"""def word_frequency(str):
    words=str.split()
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

string=input()
print(word_frequency(string))"""

#ex8
"""def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
result=fibonacci(n)
print (result)"""

#ex9
def calculate_running_average(numbers):
    summing=0
    avering=[]
    cnt=0

    for n in numbers:
        summing+=n
        cnt+=1
        average=summing/cnt
        avering.append(average)
    
    return avering

numbers = input()
numslist = list(map(int,numbers.split()))
running_avg = calculate_running_average(numslist)
print("Running averages:", running_avg)


