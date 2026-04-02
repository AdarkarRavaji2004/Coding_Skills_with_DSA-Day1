# WAP to implement conditional statement

# no = int(input("Enter any one number :"))
# if no>0:
#     print("positive number")
# if no<0:
#     print("Negative number")
# if no == 0:
#     print("number is zero")

#--------------------------------------------------------------------------
#Find Greatest number 
# n1 = int(input("Enter any 1st number :"))
# n2 = int(input("Enter any 2nd number :"))
# n3 = int(input("Enter any 3rd number :"))
# n4 = int(input("Enter any 4th number :"))
# n5 = int(input("Enter any 5th number :"))

# if n1>n2 and n1>n3 and n1>n4 and n1>n5:
#     print("The grater number is ",n1)
# if n2>n1 and n2>n3 and n2>n4 and n2>n5:
#     print("The grater number is ",n2)
# if n3>n1 and n3>n2 and n3>n4 and n3>n5:
#     print("The grater number is ",n3)
# if n4>n1 and n4>n2 and n4>n3 and n4>n5:
#     print("The grater number is ",n4)
# if n5>n1 and n5>n2 and n5>n3 and n5>n4:
#     print("The grater number is ",n5)

#--------------------------------------------------------------------------

# username = input("Enter Username : ")
# password = input("Enter Password : ")
# if username == password:
#     print("Login Successfully")
# else:
#     print("Invalid Credential")

#WAP to accept phy,chem and math subject marks calculate total and percentage and 
#if percentage is greater than equal to 60 and gender is equal to male so he is eligible for for placement else else eligible for date entry job.

# phy = int(input("Physics marks :"))
# chem = int(input("Chemistry marks :"))
# math = int(input("Maths marks :"))
# gender = input("Enter Gender male/female :")
# total = phy+chem+math
# percentage = total/3.0
# print("Total =",total)
# print("percentage",percentage)
# if percentage >= 60 and gender=="male":
#     print("you are eligible for placement")
# else:
#     print("you are eligible for data entry job")

#------------------------------------------------------------------------------------------
#WAP to accept value of A,B,C and find max value

# a = int(input("Enter Value of A :"))
# b = int(input("Enter Value of B :"))
# c = int(input("Enter Value of C :"))

# if a>b:
#     if(a>c):
#         print(a," is maximum value")
#     else:
#         print(c,"is maximum value")
# else:
#     if b>c:
#         print(b,"is maximum value")
#     else:
#         print(c,"is maximum value")

#------------------------------------------------------------------------------------
# day = input("Enter your day name : ").lower()

# if day=="saturday" or day=="sunday":
#     print("today is holiday")
# else:
#     print("today is working day")

#----------------------------------------------------------------------------------------
# #WAP to check given input is in upper case, lower case , in digit and is any symbol
# ch = ord(input("Enter any character : "))

# #ord() used to convert in ASCII code
# if ch>=65 and ch<=91:
#     print("you entered character in upper case")
# elif ch>=97 and ch<=122:
#     print("you entered character in lower case")
# elif ch>=48 and ch<=57:
#     print("you entered character in digit")
# else:
#     print("you entered character is in special symbols")

#---------------------------------------------------------------------------------------

Amount = int(input("Please Enter amount of withdraw : "))#785
print(" 100 Notes= ",Amount//100)
print(" 50 Notes= ",(Amount % 100) // 50)
print(" 20 Notes= ",((Amount % 100) % 50) // 20)
print(" 10 Notes= ",(((Amount % 100) % 50) % 20) // 10)
print(" 5 Notes = ",((((Amount % 100) % 50) % 20) % 10) // 5)