def summation(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print("Summation is : ", sum)



n=int(input("how many items: "))
mylist=[]

for i in range(1,n+1):
    i=int(input("enter {} items :" .format(i)))
    mylist.append(i)



def search(l1):
    search=int(input("which item you want to search:"))
    found=0
    foundlist=[]
    for i in range(len(l1)):
        if l1[i]==search:
            found=found+1
            foundlist.append(i)
    if found==0:
        print("not found")
    else:
        print("{} items found {} times".format(search,found))
    print("Found list is :",foundlist)

def even_odd(l2):
    evenlist=[]
    oddlist=[]
    for i in l2:
        if i%2==0:
            evenlist.append(i)
        
        elif i%2!=0:
            oddlist.append(i)
    print("even list is:",evenlist)
    print("odd list is:",oddlist)


print(mylist)
summation(mylist)
search(mylist)
even_odd(mylist)
