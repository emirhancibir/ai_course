# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:01:28 2022

@author: emirh
"""

class Calc(object):
    "calculator"
    def __init__(self, a, b):
        "initialize values"
        self.value1 = a
        self.value2 = b
        
    def add(self):
        "addition a + b = result return -> result"
        return self.value1 + self.value2
    
    def multiply(self):
        "multiplication a* b = result return -> result"
        return self.value1 * self.value2
    
print("Choose add (1)  Multiply (2)")
select = input("1 or 2 --> ")

v1 = int(input("value 1 = "))
v2 = int(input("value 2 = "))

c1 = Calc(v1, v2)

if select == "1":
    print("result --> ",c1.add())

elif select == "0":
    
    print("result --> ",c1.multiply())
    

    