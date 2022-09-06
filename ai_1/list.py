# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:21:51 2022

@author: emirh
"""

#%% dictionary
dictionary = {"kirklareli":39,"Sakarya":54}

print(dictionary.values())


#%%

#%%
liste = [1,2,3,5]
if 4 in liste:
    print("evet")
else:
    print("hayir")

#%%

#%%

def yuzyil_hesapla(yil):
    str_yil = str(yil)
    if len(str_yil) == 4:
        yuzyil = str_yil[:2]
        yuzyil = int(yuzyil)
        yuzyil = yuzyil+1
    elif len(str_yil) == 3:
        yuzyil = str_yil[:1]
        yuzyil = int(yuzyil)
        yuzyil = yuzyil+1
        
    return yuzyil

yuzyil = yuzyil_hesapla(1985)
print("{}. yuzyil".format(yuzyil))
#%%

#%%

for each in range(1,11):
    print(each)

for each in "ank ist".split():
    print(each)
    
list = [1,5,7,9,31]

count = 0

for i in list:
    count = i + count
    print(count)

count = 0
i = 0
while i < len(list):
    count  = count + list[i]
    i += 1
    print(count)
#%%

#%%
# en buyuk bulma
list = [1,5,8,120,89,91,31]

for i in list:
    enbuyuk = i
    for j in list:
        if j>enbuyuk:
            enbuyuk = j

print(enbuyuk)    



#%%


