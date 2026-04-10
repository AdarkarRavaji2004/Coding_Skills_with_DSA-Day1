#We use recursion especially in the cases we know that a problem can be divided into similar sub problems

#Factorial Solution
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))

#================================================================

# def ispalindrome(strng):
#     if len(strng)== 0:
#         return True
#     if strng[0] != [len(strng)-1]:
#         return False
#     return ispalindrome(strng[1:-1])

# print(ispalindrome("tacocat"))

#==============================================================

# def power(base , exponent):
#     if exponent == 0:     #0==0
#         return 1
#     else:
#         return base * power(base , exponent-1)
    
# print(power(2,0))
# print(power(2,2))
# print(power(2,3))
# print(power(2,4))

#===============================================================

# def capitalizeFirst(arr):

#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(["car","taco","banana"]))

#===============================================================

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])
# print(productOfArray([1,2,3]))  #6
# print(productOfArray([1,2,3,10]))#60

#============================================================
#fibonacci
# def fib(num):
#     if num < 2 :
#         return num
#     return fib(num - 1) + fib(num - 2)

# print(fib(4))
