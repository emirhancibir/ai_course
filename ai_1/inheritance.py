# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:38:09 2022

@author: emirh
"""

class Animal:
    "Parent class"    
    def __init__(self):
        print("animal is created")
    
    def to_str(self):
        print("animal")
    
    def animal_walk(self):
        print("animal walking")
        
class Monkey(Animal):
    "Child class"
    def __init__(self):
        super().__init__() # use init parent class 
        print("monkey is created")
    
    def to_str(self):
        print("Monkey")
              
    def climb(self):
        print("monkey can climb")
        
class Bird(Animal):
    "Child Class"
    def __init__(self):
        super().__init__()
        print("bird is created")
    def fly(self):
        print("bird can fly")
m1 = Monkey()
m1.animal_walk()
m1.climb()
print("--------------")
b1 = Bird()
b1.fly()