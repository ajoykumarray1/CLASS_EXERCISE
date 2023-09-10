'''
from list:
mylist=[25,15]
print("before swapping:", mylist)
temp=mylist[0]
mylist[0]=mylist[1]
mylist[1]=temp
print("after swapping:",mylist)
'''
'''
#from user input:
mylist=[]
for i in range(2):
    i=int(input("enter value:"))
    mylist.append(i)

print("before swapping:", mylist)
temp=mylist[0]
mylist[0]=mylist[1]
mylist[1]=temp
print("after swapping:",mylist)
'''
'''
mylist=[]
for i in range(2):
    i=int(input("enter {} value:".format(i)))
    mylist.append(i)

print("before swapping:", mylist)
if mylist[0]>mylist[1]:
    temp=mylist[0]
    mylist[0]=mylist[1]
    mylist[1]=temp
print("after swapping:",mylist)
'''
'''
mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    i=int(input("enter {} items :".format(i)))
    mylist.append(i)

print("my list before sorting:",mylist)
#increment loop:
for i in range(len(mylist)-1):
    for j in range(0,len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print("my list after sorting:",mylist)
'''

mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    i=int(input("enter {} items :".format(i)))
    mylist.append(i)

print("my list before sorting:",mylist)
#decrements loop:
inital=len(mylist)-1
for i in range(inital,0,-1):
    for j in range(i):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print("my list after sorting:",mylist)



