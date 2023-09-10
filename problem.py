list1=["apple", "banana", "cherry"]
list2=["Rakib", "Asim", "Sazid","Sumon"]

#append
list1.append("orange")
print(list1)
#extend
list2.extend(list1)
print(list2)
#insert
list2.insert(2,"Hasib")
print(list2)
#remove
list2.remove("Sumon")
print(list2)
#pop
list2.pop()
print(list2)
list2.pop(3)
print(list2)


