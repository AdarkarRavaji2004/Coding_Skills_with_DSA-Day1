# math = 50
# name = "Ravaji"
# pi = 3.14
# result = True
# print(type(math)) 
# print(type(name))
# print(type(pi))
# print(type(result))

#--------------------------------------------------------------------------------------------

# math = 50
# name = "Ravaji"
# pi = 3.14
# result = True
# print(id(math))   # To Show Address of variables used id()
# print(id(name))
# print(id(pi))
# print(id(result))

#--------------------------------------------------------------------------------------------

# math = 50   # new memory
# chem = 50   # same memory used for same value of variable
# physics = 40
# print(id(math))
# print(id(math))
# print(id(physics))

#------------------------------------------------------------------------------------------

# print(2+2)
# print("2"+"2")
# val1 = int(input("Enter value of val1 :")) # input() by default accept onlt string value
# val2 = int(input("Enter value of val2 :"))
# print(val1 + val2)  

#-------------------------------------------------------------------------------------------

# int()
# print(int(3.14))
# # print(int(10+5j)) # We can not convert complex value in integer
# print(int(True))
# print(int(False))
# # print(int("4.22")) # we can not convert floating point value sting to int
# print(int("4"))
# # print(int("Ravaji")) # can not convert sting name in int

#----------------------------------------------------------------------------------------------

# # float()
# print(float(3))
# # print(int(10+5j)) # We can not convert complex value in float
# print(float(True))
# print(float(False))
# print(float(4.22)) 
# print(float("4"))
# # print(int("Ravaji")) # can not convert sting name in float

#------------------------------------------------------------------------

# complex()
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# # print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))

#-----------------------------------------------------------

# bool()
# print(bool((0)))
# print(bool((15)))
# print(bool((3.14)))
# print(bool((0.0)))
# print(bool((1+2j)))
# print(bool((0+0j)))
# print(bool((-1)))
# print(bool((False)))
# print(bool((True)))
# print(bool(("ravaji")))
# print(bool())

#-------------------------------------------------------------

# There are total 33 reserve keywords in python

##Swapping values using 3 variables
# val1 = int(input("Enter the value of val1 :"))
# val2 = int(input("Enter the value of val2 :"))
# print("Before Swapping Val1= ", val1," , Val2 = ",val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("After Swapping Val1= ", val1," ,  Val2 = ",val2)

##Swaping values using 2 variables
# val1 = int(input("Enter the value of val1 :")) #10
# val2 = int(input("Enter the value of val2 :")) #30
# print("Before Swapping Val1= ", val1," , Val2 = ",val2)
# val1 = val1 + val2  #40
# val2 = val1 - val2  #10
# val1 = val1 - val2  #30
# print("After Swapping Val1= ", val1," ,  Val2 = ",val2)

#-------------------------------------------

# p1 = int(input("Wnter mark of p1 :"))
# p2 = int(input("Wnter mark of p2 :"))
# p3 = int(input("Wnter mark of p3 :"))
# total = p1+p2+p3
# percentage = total/3.0
# print("Total =",total)
# print("Percentage = ",percentage)

#---------------------------------------------------------------

# p_amount = int(input("Enter principle amount : "))#10000
# roi = int(input("Enter rate of interest: "))#10
# time = int(input("Enter the duration of loan amount : "))#1

# si = p_amount*roi*time/100
# print("Simple Interest = ",si)

#-----------------------------------------------------------------

# height = float(input("Enter Height of user in Feet : "))
# inch = height*12
# cm = inch*2.54
# print("The height of user in Inches =",inch)
# print("The height of user in cntimeters =",cm)

#----------------------------------------------------------------
#Reverse the number

# num = int(input("Enter a number :"))#123
# a = num % 10 # 3
# num = num // 10 #12

# b = num % 10 # 2
# c = num // 10 # 1

# rev = a*100+b*10+c*1
# print(rev)

#----------------------------------------------------------------------
# Identity Operator : When we want to do addresss comparison we should go for identity operator  | is , is not
# a = 10
# b = 10
# print(a is b)   # True
# print(a is not b)   #False

#--------------------------------------------------------------------------
# MemberShip Operator : By using membership operator we check that the object is present or not in collection of data structure like(list,tuple,dict,string)
# in | not in
# name = "ravaji"
# print("z" in name)
# print("z" not in name)
# print("a" in name)

#-----------------------------------------------------------------------------------------
#Control Statement