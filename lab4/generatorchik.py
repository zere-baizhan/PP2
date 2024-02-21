#ex1
"""n=int(input())
squares_generator = (i * i for i in range(n+1))
for i in squares_generator:
    print(i)"""

#ex2
# def even_num(n):
#     for num in range(n+1):
#         if num%2==0:
#             yield num

# n=int(input())
# even_gen=even_num(n)
# for num in even_gen:
#     print(num,end=", " if num!=n and num!=n-1 else "")
# print()

#ex3
# def div_num(n):
#     for num in range(n+1):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num

# n=int(input())
# divby_gen=div_num(n)
# for num in divby_gen:
#     print(num,end=", " if num!=n and num!=n-1 else "")
# print()

#ex4
# def squares(a,b):
#     for num in range(a,b):
#         yield num*num
# a=int(input())
# b=int(input())
# squares_gen=squares(a,b)
# for num in squares_gen:
#     print(num,end=", " if num!=b and num!=b-1 else "")
# print()

#ex5
def downing(n):
    for num in range(n,-1,-1):
        yield num
n=int(input())
downing_gen=downing(n)
for num in downing_gen:
    print(num,end=", " if num!=-1 else "")
print()

