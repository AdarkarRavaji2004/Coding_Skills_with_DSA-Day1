# import re       #re module for performing all the regular expression based
# count = 0       #to count the number of matching found
# pattern = re.compile("function")# string converts into bytecode
# #print(pattern)
# matcher=pattern.finditer("A function in python is defined by a def structure in function of function keyword")
# #print(matcher)
# for i in matcher: #i=3
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occerences : ",count)

#==================================================================

# import re       
# count = 0      
# matcher = re.finditer("Hi","HiHiHiHi")
# #print(matcher)
# for i in matcher: #loop 4 times execute HiHiHiHis
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occerences : ",count)

#===================================================================

# import re
# obj = input("Enter any character :")
# objmatch = re.finditer(obj,"a7b @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())

#================================================================
#match() = It always match the starting/beginning of string
# for performing match operation we need string ,this match function used to match the given pattern to starting of the string.If match is done then we will get match object else we will get None


# import re
# a = input("Enter string to perform match operation :")
# mtch = re.match(a, "python is very important language")
# print(mtch)
# if mtch != None:
#     print("match found at begining level.")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at begining level")

#==================================================================
# fullmatch : it matches the entire string

# import re
# a = input("Enter string to perform match operation :")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch != None:
#     print("Match Found")
#     print(mtch.start(),"  ",mtch.end())
# else:
#     print("Full match not found")

#====================================================================
# Search():If the match found anywhere in the string then it return object else it will return None

# import re
# a = input("Enter string to perform match operation :")
# mtch = re.search(a, "python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("There is no matching anywhere")

#-----------------------------------------------

# import re
# a = input("Enter string to perform match operation :")
# f = open('search.txt','r')
# c = f.read()
# mtch = re.search(a,c)
# print(mtch)
# if mtch != None:
#     print("match found at begining level")
#     print(mtch.start(),"  ",mtch.end(),"  ")
# else:
#     print("there is no matching ")

#===================================================================
# findall():this function return a list which containing all matches

# import re 
# mtch = re.findall('[^a-zA-Z0-9]','abch3hdh5bk7ZQ$&*')
# print(mtch)

#=====================================================================
#Sub() function - This function perform substitution or replacement 
# re.sub(expression,replacement,string)here every match pattern will be replaces by provided replacement
# import re
# mtch = re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(mtch)

#=========================================================================
#subn() function :- It is similar as sub() function only one thing is different that is also return number of replacement

# import re
# mtch = re.subn('[0-7]','@','ab3gd6nkl7')
# print(mtch)
# print("the string is= ",mtch[0])
# print("the number of relacement is=",mtch[1])

#=======================================================================
#WAP to check the valid mobile number
# import re
# mo = input("Enter mobile number :")
# obj = re.fullmatch("[0-5]\d{9}",mo)
# if obj!=None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")

#=============================================
#Write a python program to check whether the given mail id is valid gmail id or not?
# import re
# s= input("Enter Mail id :")
# m= re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m != None:
#     print("Valid E-mail Id")
# else:
#     print("Invalid E-mail id")

#========================================================

#Write a program to check whether the given file exists or not
#if available then print its content?

import os,sys
fname = input("Enter File Name :")
if os.path.isfile(fname):
    print("File exists  :",fname)
    f= open(fname,"r")
else:
    print('file does not exist: ',fname)
    sys.exit(0)
print("The content of file is :")
data = f.read()
print(data)
