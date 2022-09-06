# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:08:54 2022

@author: emirh
"""
import datetime

# parent class
class VehicleRent():
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
    
    def display_stock(self):
        print(" {} vehicle available to rent".format(self.stock))
        return self.stock
    
    def rent_hourly(self, n):
        if n<=0 :
            print("Number should be positive")
            return None
        elif n>self.stock:
            print("Sorry, {} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now
        
    def rent_daily(self, n):
        if n<=0 :
            print("Number should be positive")
            return None
        elif n>self.stock:
            print("Sorry, {} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours".format(n,self.now.hours))
            self.stock -= n
            return self.now
    
    def return_vehicle(self, request, brand):
        car_h_price = 10
        car_d_price = car_h_price*0.7*24
        bike_h_price = 5
        bike_d_price = bike_h_price*0.6*24
        
        rental_time, rental_basis, num_of_vehicle = request
        if brand == "car":
            if rental_time and rental_basis and num_of_vehicle:
                self.stock+=num_of_vehicle
                now = datetime.datetime.now()
                rental_period = now - rental_time
                
                if rental_basis == 1: # HOURLY
                    bill = rental_period.second/3600 * car_h_price*num_of_vehicle
                elif rental_basis == 2: # DAILY
                    bill = (rental_period.second/3600)*24 * car_d_price*num_of_vehicle
                
                if num_of_vehicle >= 2:
                    print("you have 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning vehicle")
                print("Price : {}$ ".format(bill))
        
        elif brand == "bike":
            if rental_time and rental_basis and num_of_vehicle:
                
                self.stock+=num_of_vehicle
                
                now = datetime.datetime.now()
                rental_period = now - rental_time
                
                if rental_basis == 1: # HOURLY
                    bill = rental_period.second/3600 * bike_h_price*num_of_vehicle
                elif rental_basis == 2: # DAILY
                    bill = (rental_period.second/3600)*24 * bike_d_price*num_of_vehicle
                
                if num_of_vehicle >= 2:
                    print("you have 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning vehicle")
                print("Price : {}$ ".format(bill))
        else:
            print("error")
    
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate =  0.15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, bill):
        bill = bill - (bill*discount_rate)
        return bill
    
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)

class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_basis_b = 0
        self.rental_time_b =0 
        
        self.cars = 0
        self.rental_basis_c = 0
        self.rental_time_c = 0
        
    
    def request_vehicle(self, brand):
        "take a request bike or car from customer"
        
        if brand == "bike":
            bikes = input("How mony bikes would you like to rent ? ")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("number should be number")
                return -1 
            
            if bikes < 1:
                print("number of bikes should be greater than 1 ")
                return -1
            
            return self.bikes
        
        elif brand == "car":
            cars = input("How mony cars would you like to rent ? ")
            
            try:
                cars = int(cars)
            except ValueError:
                print("number should be number")
                return -1 
            
            if cars < 1:
                print("number of cars should be greater or equal than 1 ")
                return -1
            
            return self.cars
        else:
            print("request vehicle error")
         
    def return_vehicle(self,brand):
        
        if brand == "bikes":
            
            if self.rental_time_b and self.rental_basis_b and self.bikes:
                return self.rental_time_b, self.rental_basis_b, self.bikes
            else:
                return 0,0,0
            
        elif brand == "cars":
            
            if self.rental_time_c and self.rental_basis_c and self.cars:
                return self.rental_time_c, self.rental_basis_c, self.cars
            else:
                return 0,0,0
        
        else:
            print("return vehicle error")
    
    
