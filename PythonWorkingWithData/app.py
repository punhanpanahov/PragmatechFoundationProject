# version 01


# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# telebeler=[adlar,soyadlar]

#while example
# i=0
# while i<len(adlar): 
#     print(f"ad:{adlar[i]}  soyad:{soyadlar[i]}")
#     i+=1

# for example
#for i in range(len(adlar)):
#    print(f"ad:{adlar[i]} soyad:{soyadlar[i]}")

# def FindFullName(ad):
#     if ad==adlar[0]:

#         print(f"telebenin tam adi {ad} {soyadlar[0]}dir")
#     if ad==adlar[1]:

#         print(f"telebenin tam adi {ad} {soyadlar[1]}dir")
#     if ad==adlar[2]:

#         print(f"telebenin tam adi {ad} {soyadlar[2]}dir")
#     if ad==adlar[3]:

#         print(f"telebenin tam adi {ad} {soyadlar[3]}dir")
#     if ad==adlar[4]:

#         print(f"telebenin tam adi {ad} {soyadlar[4]}dir")

# FindFullName("Namiq")





# version 02

#telebeler=[
#    ['Ehmed','Memmed','Sabir'],
#   ['Ehmedov','Salehov','Quliyev']
#  ]

# while example
# i=0
# while i<len(telebeler[0]):
#    print(f"ad:{telebeler[0][i]} soyad:{telebeler[1][i]}")
#    i+=1


#for example
# for i in range(len(telebeler[0])):
#    print(f"ad:{telebeler[0][i]} soyad:{telebeler[1][i]}")


# version 03

# telebe01={   
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
#     }

# telebe02={
#     "ad":"Memmed",
#     "soyad":"Salehov"
#  }

# telebe03={
#     "ad":"Sabir",
#     "soyad":"Quliyev"
#  }

# telebeler=[telebe01,telebe02,telebe03]
#while example

# i =0
# while i<3:
#     print(telebeler[i])
#     i+=1

# for example
# for e in range(len(telebeler)):
#     print(telebeler[e])
#     



#version 04

# telebeler=[
# {
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
# },
# {
#     "ad":"Memmed",
#     "soyad":"Salehov"
# },
# {
#     "ad":"Sabir",
#     "soyad":"Quliyev"
# }
# ]
#while example

# i=0
# while i<len(telebeler):
#     print(telebeler[i])
#     i+=1
#for example
# for i in (len(telebeler)):
#     print(telebeler[i])
   




# #version 05

# telebeler={
#     "adlar":['Ehmed','Memmed','Sabir'],
#     "soyadlar":['Ehmedov','Salehov','Quliyev']
# }

# i=0

# while example
# 
# while i < len(telebeler["adlar"]):
#     print(telebeler["adlar"][i],telebeler["soyadlar"][i])
#     i+=1
    
# for example
# 
# for i in (len(telebeler["adlar"])):
#     print(telebeler["adlar"][i],telebeler["soyadlar"][i])