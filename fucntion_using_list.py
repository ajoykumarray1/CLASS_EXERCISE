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

def newlist_rem(n1,n2):
    newlist=newlist1+newlist2
    print("newlist is:",newlist)
    n=2
    del list[-n:]
    print("after remove last two index in newlist is :",newlist())
    return newlist
newlist_rem(newlist1,newlist2)

add=newlist1+newlist2
newlist=newlist1+newlist2
print("newlist is:",newlist)
n=2
del newlist[-n:]
print("after remove last two index in newlist is :",newlist)



def even_odd(m1):
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
    return evenlist,oddlist,newlist

even_odd(newlist)

#even and odd
# evenlist=[]
# oddlist=[]
# for i in newlist:
#     if i%2==0:
#         evenlist.append(i)
        
#     elif i%2!=0:
#         oddlist.append(i)
# print("newlist is:", newlist)
# print("even list is:",evenlist)
# print("odd list is:",oddlist)

