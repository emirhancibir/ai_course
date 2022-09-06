# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:40:51 2022

@author: emirh
"""
#%%
class Square(object):
    
    edge = 5
    area = 0
    
    def calc_area(self):
        self.area = self.edge*self.edge
        print(self.area)
s1 = Square()
s1.edge = 15

s1.calc_area()
#%%

#%%
class Employee(object):
    age = 35
    salary = 3000

    # method
    def age_salary_ratio(self):
        res = self.age / self.salary
        print(res)
        return res
e1 = Employee()
res = e1.age_salary_ratio()

# function

def age_salary_ratio(age,salary):
    print("func : ",age/salary)

age_salary_ratio(15, 1500)
#%%

#%%

class Animal(object):
    """
    a = name b= age
    """
    # cstor
    def __init__(self, a, b):
        self.name = a
        self.age = b
    
    def get_name(self):
        print(self.name)
        return self.name
    
    def get_age(self):
        print(self.age)
        return self.age

a1 = Animal("dog", 3)

a1.get_name()

























#%%
