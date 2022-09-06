# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:57:31 2022

@author: emirh
"""

class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def login_info(self):
        print(self.name + " " + self.surname)

class Website2(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
    def login(self):
        print(self.name + " " + str(self.ids))
        
w1 = Website2("name", "surname", 15)
w1.login_info()
w1.login()
