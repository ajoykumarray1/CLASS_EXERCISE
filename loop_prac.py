Daffodil_Bugs=["Pritom Sarkar","Shazid Hasan","Md. Fakrul Islam","Tahmina Sultana", "Md.Milon Raza"]
DIPTI_Pydantic=["Joy Ahmed","MD Ahaduzzaman","Rupa Chakma","Al Arman Bejoy","MD Lokman"]
Pythoneers=["Ahnaf Tahmeed","Abrar Karim","Erfanul Haque","Farjana Tasnim","Sumiya Rasid"]
JSRM_Unity=["Jilan Chowdhury","Mishan Kahisa","Sumaiya Akter Sima","MD. RASHEL MIA"]
Hungrybirds=["Ajoy Kumar Ray","Md. Rakib Ahmed Sazid","Md.Hasib","Mehedi Hasan","Faiad Farhan"]
teamlist=[Daffodil_Bugs,DIPTI_Pydantic,Pythoneers,JSRM_Unity,Hungrybirds]
newlist=[]
nlist=[]

for i in range(len(teamlist)):
    for j in teamlist[i]:
        if j=="Mishan Kahisa" or j=="Sumaiya Akter Sima":
            continue
        newlist.append(j)
print(newlist)

# for i in teamlist:
#     if i==JSRM_Unity:
#         continue
#     newlist.append(i)
# #print(newlist)

# for i in newlist:
#     for j in i:
#         nlist.append(j)
# print(nlist)


        

# for i in Daffodil_Bugs,DIPTI_Pydantic,Pythoneers,JSRM_Unity,Hungrybirds:
#     teamlist.append(i)

# # print(teamlist)

# # for i in teamlist:
# #     for j in i:
# #         newlist.append(j)
# # print(newlist)

# for i in range():
#     for j in i:
#         newlist.append(j)
# print(newlist)