# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:11:51 2022

@author: emirh
"""

from abc import ABC , abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def run(self):
        pass

class Bird(Animal):
    
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")

    def run(self):
        print("ruuun!")


b1 = Bird()
b1.walk()