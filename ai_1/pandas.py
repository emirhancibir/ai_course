# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:46:58 2022

@author: emirh
"""

import pandas as pd
#%%
dictionary = {"NAME":["ali","osman","yigit","kenan","ayse","sinan"],
              "AGE": [15,16,33,25,12,14],
              "MAAS":[100,200,350,550,750,400]}

data_frame_1 = pd.DataFrame(dictionary)
head = data_frame_1.head()
tail = data_frame_1.tail()
#%%

#%%
# pandas basics

print(data_frame_1.columns)
print(data_frame_1.info())
print("-----------------")
print(data_frame_1.dtypes)
print("-----------------")
print(data_frame_1.describe())
#%%

#%%
# print(data_frame_1["AGE"])
# print(data_frame_1.AGE)

data_frame_1["new feature"] = [-1,-2,-3,-4,-5,-6]

print(data_frame_1.loc[:3,"AGE":"MAAS"])
print(data_frame_1.loc[:3,["AGE","NAME"]])
print(data_frame_1.loc[::-1,:])
print("-----------------")
print(data_frame_1.loc[:,"NAME"])
print("-----------------")
print(data_frame_1.iloc[:,2]) # tum satirlar ve indexi 2 olan sütün

#%%

#%%
# filtering

filter1 = data_frame_1.MAAS > 200

# print(type(filter1))
# <class 'pandas.core.series.Series'>
# only greater than 200 salary
filtered_data = data_frame_1[filter1]

filter2 = filtered_data.AGE < 20

# yas<20 maas>200
# filtered_data2 = filtered_data[filter2]
filtered_data2 = data_frame_1[filter1 & filter2]

print(data_frame_1[data_frame_1.AGE > 30])

#%%

#%% list comprehension
import numpy as np

mean_maas = data_frame_1.maas.mean() # 391.6666666666667
mean_maas2 = np.mean(data_frame_1.maas)

data_frame_1["MAAS_LEVEL"] = ["yuksek" if i >= mean_maas else "dusuk" for i in data_frame_1.maas]

data_frame_1.columns = [i.lower() for i in data_frame_1.columns]

data_frame_1.columns = [i.split()[0]+"_"+i.split()[1] if len(i.split()) >= 2 else i for i in data_frame_1.columns]

#%%

#%%
# drop and concatenating data
# data_frame_1.drop(["new_feature"],axis=1, inplace=True)
# axis 1 sutun drop eder
# axis 0 satir drop eder
# inplace true -> dataframe1 e esitler

data1 = data_frame_1.head()
data2 = data_frame_1.tail()

# vertical concat
data_concat = pd.concat([data1,data2],axis=0)
# axis 0 satır olarak altına ekler

# horizontal concat
maas = data_frame_1.maas
age = data_frame_1.age
dat_h_concat = pd.concat([maas, age],axis = 1)

#%%

#%% transforming data

data_frame_1["double_age"] = [2*i for i in data_frame_1.age]
# apply

def multiply(age):
    return age*3

data_frame_1["triple_age"] = data_frame_1.age.apply(multiply)



#%%
