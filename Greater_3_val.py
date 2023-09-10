'''
a=10
b=5
c=20

if a>b and a>c:
    print("a is greater than b,c")
elif b>a and b>c:
    print("b is greater than a,c")
else:
    print("c is greater than a,b")
'''
'''
a , b , c = int(input("Enter value a:")),int(input("Enter value b:")),int(input("Enter value c:"))
if a>b and a>c:
    print("a is greater than b,c")
elif b>a and b>c:
    print("b is greater than a,c")
else:
    print("c is greater than a,b")


'''
a , b , c, d = int(input("Enter value a:")),int(input("Enter value b:")),int(input("Enter value c:")),int(input("Enter value d:"))

if a>b:
    if a>c:
        if a>d:
            print("a is grater than b,c and d")
        else:
            print("d is grater than a,b and c")
    else:
        if c>d:
            print("c is grater than a,b and d")
        else:
            print("d is grater than a,b and c")

else:
    if b>c:
        if b>d:
            print("b is greater than a,c and d")
        else:
            print("d is greater than a,b and c")
    else:
        if c>d:
            print("c is grater than a,b and d")
        else:
            print("d is grater than a,b and c")
