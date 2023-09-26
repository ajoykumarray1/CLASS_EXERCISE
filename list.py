# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)
# print(thislist[5])
# print(thislist[:])
# print(thislist[:5])
# print(thislist[2:5])
# print(thislist[:-1])
# print(thislist[-5:-1])
# print(thislist[-1:])


number=[10,22,38,21,99,20]
even=[]
odd=[]

for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
    