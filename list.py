#-----------------------List-------------------------------------------------
# mylist = ["prashant","ravaji","vivek","ankush",77,True,60.52,"prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

#---------------Change the Value--------------------------------------------
# mylist[2]="Omkar"
# print(mylist)

# if "ravaji" in mylist:
#     print("yes, Ravaji is available")
# else:
#     print("Not available")

#----------------append()----------------------------------------------------
# mylist.append("harsh")
# mylist.append('laxuman')
# print(mylist)

#------------to add item at specified position-------------------------------
# mylist.insert(1,"sanket")
# print(mylist)

#------------------remove()-------------------------------------------------
# mylist.remove("vivek")
# print(mylist)

#------------------copy()----------------------------------------------------
# newlist = mylist.copy()
# print(mylist)
# print("Copylist :",newlist)

#--------------------------------------------------------------------------------------------------------------
#-------------------Nested-list(Multi Dimentional list)-----------------
# mylist = [["prashant","jha"],["85.56"],[440022,"yyy"]]
# print("Example of Multidimentional list :")
# print(mylist)
# ## print(mylist[row][col])
# print(mylist[0][0]) #'prashant'
# print(mylist[0][1]) #'jha'
# print(mylist[1][0]) #85.56
# print(mylist[2][0]) #440022
# print(mylist[2][1]) #'yyy'

#-------------------------------------------------------------------------------
# list1 = ["ravaji","adarkar"]
# print(list1*2)          #It will print Two times
# list2 = [50,25.50]
# print(list1+list2)

#-------------------------------------------------------------------------------
# list2 =[50,25.50,"prashant"]
# del list2[2]
# # del list2
# print(list2)

#----------------------------------------------------------------------------------
# list2 =[50,25.50,"prashant"]
# print(list2)
# list2.clear()
# print(list2)

#---------------------------------------------------------------------------------
# name = "ravaji" #str
# print(name)
# myname = list(name) #Typecasting
# print(myname)

#-------------------------------------------------------------------------------
# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

#------------------------------------------------------------------------------
# mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

#--------------------------------------------------------------------------------
# mylist = [44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[1]="prashant"
# print(mylist)
# print(newlist)

#----------------------------------------------------------------------------------
# arr =[[1,2,3,4],
#       [4,5,6,7],
#       [8,9,10,11],
#       [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop()) #Output = 4,7,11,15

#----------------------------------------------------------------------------------
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")   #Output = 2,3,4,5,6,6

#------------------------------------------------------------------------------------
# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

#-------------------------------------------------------------------------------------
# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

#-----------------------------------------------------------------------------------
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

#-----------------------------------------------------------------------------------
