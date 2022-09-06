# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:45:36 2022

@author: emirh
"""

# %%
# variable

var1 = 10
var2 = 15 

gun = "pazartesi"

var3 = 10.0
print(var1)
#%%

#%%
#numbers
integer1 = -50

double_1 = -30.7

#%%

#%%
# default and flexible func

# default func
def cember_cevre(r,pi=3.14):
    """
    default function pi default olarak ayarlandı
    """
    out = 2*pi*r
    return out

#flexible func
def hesapla(boy,kilo,*args):
    output = (boy+kilo)*args[0]
    return output
#%%

#%%
#Quiz
yas = 10
isim = "ali"
soyisim = "veli"

def function_quiz(yas,isim,*args,ayakkabi_no=35):
    print("Cocugun yasi : ", yas)
    output = args[0]*yas
    return output

sonuc = function_quiz(yas, isim, soyisim)

print(sonuc)

#%%

#%%
# lambda function
def hesapla1(x):
    out = x*x
    return out

result = hesapla1(5)
print(result)

result2 = lambda x: x*x

print(result2(5))


#%%














