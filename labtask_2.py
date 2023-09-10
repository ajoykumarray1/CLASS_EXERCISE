# 1. Create a Function with Your Name. the Function Print your Name, Address, Mobile Number and Age.

def Ajoy():
    n=(input("enter name:"))
    a=(input("enter address:"))
    m=(input("enter mobile no:"))
    age=int(input("enter age:"))

    print("My name is:"+n)
    print("My address is:"+a)
    print("My mobile number is:"+m)
    print("My age is:" +age)
    
Ajoy()

# 2. Take a list from user, the list contain your Mobile Number and find out the Max and Min number from the list.Create separate function to find out Max and Min.


mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    tem=int(input("enter {} items :".format(i)))
    mylist.append(tem)
print("this list is:",mylist)
#max in list:
def maximum(l):
    max1=l[0]
    for m in l:
        if m>max1:
            max1=m
    print("maximum number of list is:",max1)



#min in list:
def minimum(m):
    min1=m[0]
    for o in m:
        if o<min1:
            min1=o
    print("minmum number of list is:",min1)

maximum(mylist)
minimum(mylist)


#3. Take a list from user, the list contain your Mobile Number and sort the list with ascending order.
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


#4. Take a list from user, the list contain your Mobile Number and find out the Even Numbers List and Odd Number List.
mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    i=int(input("enter {} items :".format(i)))
    mylist.append(i)

def even_odd(m1):
    evenlist=[]
    oddlist=[]
    for i in m1:
        if i%2==0:
            evenlist.append(i)
        elif i%2!=0:
            oddlist.append(i)
    print("newlist is:", mylist)
    print("even list is:",evenlist)
    print("odd list is:",oddlist)
    return evenlist,oddlist,mylist

even_odd(mylist)

# 5. Take a number from user and check the number is prime or not prime.

def isPrime(num):
    count=0
    for i in range(2,num):
        if num%i==0:
            count=1
    if count==0:
        print("Prime")
    else:
        print("not Prime")

myNumber=int(input("enter a Number to check isPrime:"))
isPrime(myNumber)