Daffodil_Bugs=["Pritom Sarkar","Shazid Hasan","Md. Fakrul Islam","Tahmina Sultana", "Md.Milon Raza"]
DIPTI_Pydantic=["Joy Ahmed","MD Ahaduzzaman","Rupa Chakma","Al Arman Bejoy","MD Lokman"]
Pythoneers=["Ahnaf Tahmeed","Abrar Karim","Erfanul Haque","Farjana Tasnim","Sumiya Rasid"]
JSRM_Unity=["Jilan Chowdhury","Mishan Kahisa","Sumaiya Akter Sima","MD. RASHEL MIA"]
Hungrybirds=["Ajoy Kumar Ray","Md. Rakib Ahmed Sazid","Md.Hasib","Mehedi Hasan","Faiad Farhan"]

# for i in Daffodil_Bugs:
#     if "Md. Fakrul Islam" in i:
#         break
#     print(i)
# for i in Daffodil_Bugs:
#     if "Md. Fakrul Islam" in i:
#         continue
#     print(i)



newlist=[]
Daffodil_Bugs.extend(DIPTI_Pydantic)
print(Daffodil_Bugs)
Daffodil_Bugs.extend(Pythoneers)
print(Daffodil_Bugs)
Daffodil_Bugs.extend(JSRM_Unity)
print(Daffodil_Bugs)
Daffodil_Bugs.extend(Hungrybirds)
print(Daffodil_Bugs)

for i in Daffodil_Bugs:
    if "A" in i:
        newlist.append(i)
print(newlist)
# Teamlist=[]

#or..............
# Teamlist.extend(Daffodil_Bugs)
# Teamlist.extend(DIPTI_Pydantic)
# Teamlist.extend(Pythoneers)
# Teamlist.extend(JSRM_Unity)
# Teamlist.extend(Hungrybirds)
# print(Teamlist)

# for i in Daffodil_Bugs:
#      if "A" in i:
#         newlist.append(i)
# print(newlist)


#or.............
# for i in Daffodil_Bugs:
#     Teamlist.append(i)
# for i in DIPTI_Pydantic:
#     Teamlist.append(i)
# for i in Pythoneers:
#     Teamlist.append(i)
# for i in JSRM_Unity:
#     Teamlist.append(i)
# for i in Hungrybirds:
#     Teamlist.append(i)
# print(Teamlist)
# for i in Daffodil_Bugs:
#      if "A" in i:
#         newlist.append(i)
# print(newlist)

# clist=Daffodil_Bugs+DIPTI_Pydantic+Pythoneers+JSRM_Unity+Hungrybirds

# for i in clist:
#      if "A" in i:
#         newlist.append(i)
# print(newlist)

# for i in range(101):
#     if i%2==0: 
#       continue
#     print(i)
# for i in range(1,101,2):
#     if i%2!=0 and i==61: 
#       break
#     print(i)

# for i in range(100):
#     if i%2!=0:
#         print(i)
#         continue
#     if i>=60:
#         break
    