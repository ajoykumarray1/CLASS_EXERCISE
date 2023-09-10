list=int(input("How many items in list is:"))
print("list item contains:", list)
newlist=[]
for i in range(list):
    i=int(input("enter number:"))
    newlist.append(i)
evenlist=[]
oddlist=[]
for i in newlist:
    if i%2==0:
        evenlist.append(i)
        
    elif i%2!=0:
        oddlist.append(i)
print("newlist is:", newlist)
print("even list is ",evenlist)
print("odd list is",oddlist)


#using max function:
print("largest number of the newlist is:", max(newlist))
print("largest number of the evenlist is:", max(evenlist))
print("largest number of the oddlist is:", max(oddlist))

max=newlist[0]
for n in newlist:
    if n>max:
        max=n
print("largest number of newlist using for loop is:",n)


max1=evenlist[0]
for m in evenlist:
    if m>max1:
        max1=m
print("largest number of evenlist using for loop is:",m)

max2=oddlist[0]
for o in oddlist:
    if o>max2:
        max2=o
print("largest number of oddlist using for loop is:",o)



   