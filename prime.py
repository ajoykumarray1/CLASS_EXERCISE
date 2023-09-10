# def isPrime(num):
#     count=0
#     for i in range(2,num):
#         if num%i==0:
#             count=1
#     if count==0:
#         print("Prime")
#     else:
#         print("not Prime")

# myNumber=int(input("enter a Number to check isPrime:"))
# isPrime(myNumber)


#or solved by another way

num=int(input("enter number to check Prime or not Prime :"))
if num==1:
    print("not prime")

elif num>1:
    ajoy=False
    for i in range(2,int(num/2)):  #we can write for i in range(2,num)
        if num%i==0:
            ajoy=True
    if ajoy:
        print("not Prime")
    else:
        print("Prime")

