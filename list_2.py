thislist=["apple", "banana", "cherry"]
list1=["Rahim", "Karim", "Abdul"]
list1.append("Bashar")
list1.extend(thislist)
list1.insert(2,"Public")
thislist.extend(list1)
print(thislist)
print(list1)