# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:54:47 2022

@author: emirh
"""

import pandas as pd

df = pd.read_csv("iris.csv")

# print(df.columns)
# """
# Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',
#        'Species'],
#       dtype='object')
# """
# print("----------------")
# print(df.Species.unique())
# """
# ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
# """
# print("----------------")
# print(df.info())
# print("----------------")
# print(df.describe())

# setosa = df[df.Species == "Iris-setosa"]
# versicolor = df[df.Species == "Iris-versicolor"]


# print(setosa.describe())
# print(versicolor.describe())

#%%
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)
# df1.plot()
# plt.show()
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor" )
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica" )
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.grid(ls = "-", alpha = 0.4)
plt.show()

#%%

#%% scatter plot
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "blue", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color = "red", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "green", label = "virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.legend()
plt.show()
#%%

#%% histogram

plt.hist(setosa.PetalLengthCm, bins = 15)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frequency")
plt.title("Hist")
plt.legend()
plt.show()

#%%

#%% bar plot

import numpy as np

x = np.array([1,2,3,4,5])

y = x *2

plt.bar(x, y)
plt.title("bar plot")
plt.show()

#%%

#%% subplot
df1.plot(grid = True, alpha = 0.9,subplots = True )
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")

plt.subplot(2,1,2)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor" )

plt.show()








#%%