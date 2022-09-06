# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:19:06 2022

@author: emirh
"""

class BankAccount(object):
    
    def __init__(self,name,money,address):
        self.name = name # global
        self.__money = money # private sadece class icinde kullanilir
        self.address = address
    
    # create getter and setter
    def get_money(self):
        return self.__money
    
    def set_money(self, amount):
        "set money of person"
        self.__money = amount
    def __increase_500(self):
        "sadece class icinde cagirilabilir private method"
        self.__money = self.__money + 500

p1 = BankAccount("messi", 1000, "barca")

print(p1.get_money())
p1.set_money(1500)
print(p1.get_money())