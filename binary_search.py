mylist=[]
Number=int(input("Enter list length :"))

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
Search=int(input("which item you want to search:"))
found=0
left,right=0,len(mylist)-1
while(left<=right):
    mid=(left+right)//2

    if mylist[mid]==Search:
        found=1
        break
    elif mylist[mid]<Search:
        left=mid+1
    else:
        right=mid-1
if found:
    print("Found")
else:
    print("Not found")