# Sting :
# name =    "ravajiadark"
# #indexing= 012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# # print(name[15]) #Error String index out of range
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

#---------------------------------------------------------------------------------------------------------
#String Define Function()

# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#-------------------------------------------------------------------------------------------------------------
#Format Specifier :

# print("Subject Marks :")
# phy = 50
# chem = 60
# math = 70
# print("physics={} chemistry={} math={}".format(phy,chem,math))
# print("physics={0} chemistry={1} math={2}".format(phy,chem,math))
# print("physics={x} chemistry={y} math={z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks :",f"{total}")
# print("Roll No =","7".zfill(4))

#----------------------------------------------------------------------------------------------------
# for(initialization; condition; inc/dec)

# for i in range(1,10,2):
#     print(i)

#Table :
# for i in range(1,11):
#     print(i,"\t",i*2,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10)
# print("-----------------------------------------------------------------------------")
# for i in range(1,11):
#     print(i*11,"\t",i*12,"\t",i*13,"\t",i*14,"\t",i*15,"\t",i*16,"\t",i*17,"\t",i*18,"\t",i*19,"\t",i*20)

#--------------------------------------------------------------------------------------------------

# name = "racear"
# for i in name:
#     print(i)

#-------------------------------------------------------------------------------------------------

#WAP to remove duplicate
# name = "racear"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname+=i
# print(name)
# print(newname)

#--------------------------------------------------------------------------------------------------
#Reverse 
# for i in range(5,-1,-1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

#--------------------------------------------------------------------------------------------------
#WAP to Reverse the string using for loop
# name = "Mumbai"
# newname =""
# n = len(name)
# for i in range(n-1,-1,-1):
#     newname+=name[i]
# print(newname)

#------OR--------
# name = "Mumbai"
# newname =""
# for i in name:
#     newname = i + newname
# print(newname)

#---------------------------------------------------------------------------------------------------------
#WAP to check if a given string is palindrome using loop
# string = "racecar"
# print(string)
# print(string[::-1])

#--------------------------------------------------------------------------------------------------
# if string == string[::-1]:
#     print("plaindrome string")
# else:
#     print("Not palindrome string")

#----------------------------------------------------------------------------------------------------
#Collection Datatype
#list

#--------------------------------------------------------------------------------------------------
# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

#--------------------------------------------------------------------------------------------------

# a =[4,0,2,5,0,1]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)
# print(a)

#--------------Remove Duplicate-------------------------------------------------------------------
# list =[1,2,2,3,4,4,5]
# newlist =[]
# for i in list:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

#-------------------------------------------------------------------------------------------------
#print common element in the lists

# list1 = [1,2,3]
# list2 = [2,3,4]
# list3 = [3,4,5]
# for i in list1:
#     if i in list2 and i in list3:
#         print(i)

#-------------------------------------------------------------------------------------------------
# n = int(input("Enter size of array :"))
# arr=[]
# for i in range(n):
#     val = int(input('Enter the vvalue of array :'))
#     arr.append(val)
# sum =0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum+=abs(arr[i] - arr[i+1])
# print(sum)

#-------------------------------------------------------------------------------------------------

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i," ",j)

#--------------------------------------------------------------------------------------------------
#WAP to move

# name = "prashant*is*a*good*programmer"
# newname=''
# val=''
# for i in name:
#     if i !='*':
#         newname+=i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))

#-------------------------------------------------------------------------------------------------
#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)
#-------------------------------------------------------------------------------------------------
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

#-------------------------------------------------------------------------------------------------

#WAP to check "listen" and "silent" are anagram
# str1 ="listen"
# str2 ="silent"
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#-------------------------------------------------------------------------------------------------
#WAP To count number of words in string
# str1 = "This is a sentence"
# count =1
# for i in str1:
#     if i == ' ':
#         count+=1
# print(count)

#------------------------------------------------------------------------------------------------
#Product of Array Except Self:
#Given an array ,return an aarray where each element is the product of all element in the array except itself

# arr = [1,2,3,4]
# output = []
# for i in range(len(arr)):
#     product = 1
#     for j in range(len(arr)):
#         if i != j:
#             product *= arr[j]
#     output.append(product)
# print(output)