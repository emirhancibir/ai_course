# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:11:16 2022

@author: emirh
"""

class Animal:
    
    def to_str(self):
        print("Animal")

class Monkey(Animal):
    
    def to_str(self):
        print("monkey")

a1 = Animal()
a1.to_str()

m1 = Monkey()
m1.to_str()