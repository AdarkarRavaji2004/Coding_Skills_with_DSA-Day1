#Write a program to reverse each word in a string
#Sample Input: "Hello World"
#Expected Output: "olleH dlroW"

# string = "Hello World"

# words = string.split()          # Split string into words
# print(words)
# reversed_words = []

# for word in words:
#     reversed_words.append(word[::-1])   # Reverse each word

# print(reversed_words)
# result = " ".join(reversed_words)       # Join words back into string

# print(result)

#-----------------------------------------------------------------------------------------
#Write a program to compress a string by replacing consecutice caracters with their counts
#Sample Input: "aaabbbcccc"
#Expected Output: "a3b3c4"

# string = "aaabbbcccc"

# result = ""
# count = 1

# for i in range(len(string)):
#     if i < len(string) - 1 and string[i] == string[i + 1]:
#         count += 1
#     else:
#         result += string[i] + str(count)
#         count = 1

# print(result)

#============================================================================================

# from abc import ABC, abstractmethod
# class Help4Code(ABC):
#     @abstractmethod
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(self):
#         pass

# class Ashish(Help4Code):
#     def training(self):
#         print("C,C++,Java")

#     def placement(self):
#         print("Java Placement")

# class Ankush(Help4Code):
#     def training(self):
#         print("Python | Django")

#     def placement(self):
#         print("Python Placement Students")

# class Prashant(Help4Code):
#     def training(self):
#         print("Machine Learning ")

#     def placement(self):
#         print("Data Science Placement")

# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Prashant()
# obj3.training()
# obj3.placement()

#============================================================================================

# from abc import ABC, abstractmethod 
# class Irctc(ABC):
#     @abstractmethod
#     def bookTicket(self):
#         pass

# class MakeMyTrip(Irctc):
#     def bookTicket(self):
#         print("=======================================")
#         print("      Welcome to maketrip.com       ")
#         source = input("Enter a Source station name: ")
#         destination = input("Enter Destination name: ")
#         date = input("Enter Date of Journey: ")
#         print("=======================================")

# class GoIbibo(Irctc):
#     def bookTicket(self):
#         print("=======================================")
#         print("      Welcome to Goibibo.com       ")
#         source = input("Enter a Source station name: ")
#         destination = input("Enter Destination name: ")
#         date = input("Enter Date of Journey: ")
#         print("=======================================")

# class Yatra(Irctc):
#     def bookTicket(self):
#         print("=======================================")
#         print("      Welcome to Yatra.com       ")
#         source = input("Enter a Source station name: ")
#         destination = input("Enter Destination name: ")
#         date = input("Enter Date of Journey: ")
#         print("=======================================")

# obj1 = MakeMyTrip()
# obj1.bookTicket()
# obj2 = GoIbibo()
# obj2.bookTicket()
# obj3 = Yatra()
# obj3.bookTicket()   

#============================================================================================
#Encapsulation => Wrapping data and methods into a single unit (class) and restricting access to some of the object's components.

# class Base: #parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "prashant" #public variable    
#         self.__c = "ankush" #private variable
# #Creatind a derived class
# class Derived(Base): #child class
#     def __init__(self):
#         #Calling constructor of base class
#         Base.__init__(self)
#         # print("calling private member of base class")
#         # print(self.a) 
#         # print(self.__c) 
        
# # obj1 = Derived()
# # print(obj1.a) 
# # print(obj1.__c)    
# obj2 = Base() 
# print(obj2.a)       #Accessible
# print(obj2.__c)     #Not Accessible
        
#============================================================================================

# class Rbi:
#     #Declaring public method
#     def publicPolicy(self):
#         print("Check the public policy of RBI")

#     #Declaring private method
#     def __privatePolicy(self):
#         print("There is some private policy which is not accessible for public")

# class Sbi(Rbi):
#     def __init__(self):     #first sbi class constructor called
#         Rbi.__init__(self)  #second parent class constructor called

#     def callingPublicMethod(self):  #child class public method
#         print("\nInside child class")
#         self.publicPolicy()  #Calling parent class public method

#     def callingPrivateMethod(self): #child class private method
#         self.__privatePolicy() #Calling parent class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()  
# obj1.callingPrivateMethod()  
# obj1.publicPolicy()          
# obj1.__privatePolicy() 

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy() 
# obj2._Rbi__privatePolicy()

#============================================================================================
#All the even numbers are placed before all the odd numbers
# Sample Input: 10 98 3 33 12 22 21 11
#Expected Output: 10 98 12 22 3 33 21 11

# list = [10,98,3,33,12,22,21,11]
# even = []
# odd = []

# for i in list:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# newlist = even+odd
# print(list)
# print(newlist)

#============================================================================================
