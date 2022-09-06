# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:39:47 2022

@author: emirh
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    "abstract super class"
    
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

    # overriding polymorphism
    def to_str(self): pass

# child class

class Square(Shape):
    "sub class"
    
    def __init__(self,edge):
        self.__edge = edge # encapsulation
   
    def area(self): 
        result = self.__edge ** 2
        print("Square area", result)
    
    def perimeter(self):
        result = self.__edge* 4
        print("Square perimeter", result)
        
class Circle(Shape):
    pi = 3.14
    
    def __init__(self, radius):
        self.__radius = radius
        
    def area(self): 
        result = self.__radius ** 2 * self.pi
        print("circle area", result)
    
    def perimeter(self):
        result = self.__radius* 2*self.pi
        print("circle perimeter", result)


c = Circle(5)
c.area()
    