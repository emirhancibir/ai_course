# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 22:40:38 2022

@author: emirh
"""

class Calisan:
    
    zam_oran = 1.8 # class variable
    counter = 0
    def __init__(self,name,surname,maas):
        self.name = name
        self.surname = surname
        self.maas = maas
        self.email = name+surname+"@adasd.com"
        
        Calisan.counter = Calisan.counter +1 
    def give_name_surname(self):
        return self.name + " " +self.surname
    
    def zam_yap(self):
        self.maas = self.maas +self.maas *self.zam_oran
        
# isci1 = Calisan("name", "surname", "email@asad.com")

# print(isci1.name)

calisan1 = Calisan("akdo", "skrr", 100)
print(Calisan.counter)
# print("ilk maas",calisan1.maas)
# calisan1.zam_yap()
# print("zamli maas",calisan1.maas)
calisan2 = Calisan("name", "surname", 131)
print(Calisan.counter)
calisan3 = Calisan("as", "ma", 120)
calisan4 = Calisan("aw", "rooo", 1310)

liste = [calisan1,calisan2,calisan3,calisan4]

max_maas = calisan2.maas
for i in liste:
    if i.maas > max_maas:
        max_maas = i.maas
        max_maas_index = i
print(max_maas)
print(max_maas_index.give_name_surname())
