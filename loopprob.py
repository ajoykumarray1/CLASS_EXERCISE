list1=int(input("How many items in list1 is:"))
list2=int(input("How many items in list2 is:"))
print("list item contains:", list1)
print("list item contains:", list2)
newlist1=[]
newlist2=[]
for i in range(list1):
    i=int(input("enter number in list1:"))
    newlist1.append(i)
print("newlist1 is:",newlist1)
for j in range(list2):
    j=int(input("enter number in list2:"))
    newlist2.append(j)
print("newlist2 is:",newlist2)

#add newlist1+newlist2
newlist=newlist1+newlist2
print("newlist is:",newlist)
n=2
del newlist[-n:]
print("after remove last two index in newlist is :",newlist)

#even and odd
evenlist=[]
oddlist=[]
for i in newlist:
    if i%2==0:
        evenlist.append(i)
        
    elif i%2!=0:
        oddlist.append(i)
print("newlist is:", newlist)
print("even list is:",evenlist)
print("odd list is:",oddlist)

#Max number of newlist, evenlist,oddlist
minn=newlist[0]
for i in newlist:
    if i<minn:
        minn=i
print("minimum number of newlist using for loop is:",minn)


min1=evenlist[0]
for i in evenlist:
    if i<min1:
        min1=i
print("minimum number of evenlist using for loop is:",min1)

min2=oddlist[0]
for i in oddlist:
    if i<min2:
        min2=i
print("minimum number of oddlist using for loop is:",min2)