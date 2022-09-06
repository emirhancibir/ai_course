# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:21:58 2022

@author: emirh
"""

class Employee():
    
    def raisee(self):
        raise_rate = 0.1
        res = 100+ 100*raise_rate
        print("employee", res)

class Ceng():
    
    def raisee(self):
        raise_rate = 0.2
        res = 100+ 100*raise_rate
        print("ceng", res)
        
class Eeeng():

    def raisee(self):
        raise_rate = 0.5
        res = 100+ 100*raise_rate
        print("eeeng", res)    
        
e1 = Employee()
c1 = Ceng()
ee1 = Eeeng()

employee_list = [e1,c1,ee1]

for i in employee_list:
    i.raisee()