# myList=["Apple","Cherry","Kiwi","Banana"]
# myList2=["Red","Green","Yellow","Magenta"]


#print(myList)
'''
for i in myList:
    print(i)
myListLenght=len(myList)
myList2Lenght=len(myList2)

print("First List Length is:",myListLenght)
print("First List Lenght is:",myList2Lenght)
 
for i in range(myListLenght):
    print(myList[i])
'''
    
# for i in myList2:
#     if "A" in i:
#         print(i)

# for i in myList:
#     if "A" in i or "C" in i:
#         print(i)

# newlist=[]
# for i in myList:
#     if "a" in i:
#         newlist.append(i)
#         print(newlist)

# mylist1=["Apple","Cherry","Kiwi","Banana"]
# mylist2=["Red","Green","Yellow","Magenta"]
# mylist1.extend(mylist2)
# mylist=mylist1.copy()
# print(mylist)

# newlist=[]
# for i in mylist:
#     if "a" in i:
#         newlist.append(i)
#         print(newlist)

list1=["Red","Green",["Gray","Lime","Levender"],["Rahim","['Karim']"],[1,2,3],[True,False]]
print(list1[2][2])
color=[]
numbering=[]
boolean=[]
color=list1[2]
print(color)
numbering=list1[3]
print(numbering)
boolean=list1[4]
print(boolean)
