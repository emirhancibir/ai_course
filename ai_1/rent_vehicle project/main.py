# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:17:13 2022

@author: emirh
"""

from rent import CarRent, BikeRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while 1:
    if main_menu:
        print("""
              ***** Vehicle Rental Shop *****
              A. Bike Menu
              B. Car Menu
              Q. Exit""")
        main_menu = False
        
        choice = input("Enter Choice : ")
        
        if choice == "A" or "a":
            print("""
                  ***** BIKE MENU *****
                  1. Display available bikes
                  2. Request a bike on hourly basis 
                  3. Request a bike on daily basis 84 $
                  4. Return a vehicle
                  5. Main Menu
                  6. Exit
                  """)
            choice = input("Enter Choice : ")
            
            try:
                choice = int(choice)
            except ValueError:
                print("its not int") 
                continue
            
            if choice == 1:
                
                bike.display_stock()
                choice = "A"
            
            elif choice == 2:
                customer.rental_basis_b = bike.rent_hourly(customer.request_vehicle("bike"))
                customer.rental_basis_b = 1
                main_menu = True
                print("--------------------")
            
            elif choice == 3:
                customer.rental_basis_b = bike.rent_daily(customer.request_vehicle("bike"))
                customer.rental_basis_b = 2
                main_menu = True
                print("--------------------")
            
            elif choice == 4:
                customer.bill = bike.return_vehicle(customer.return_vehicle("bike"), "bike")
                customer.rental_basis_b, customer.rental_time_b, customer.bikes = 0,0,0
                main_menu = True
            
            elif choice == 5 :
                main_menu = True
           
            elif choice == 6:
                break
            
            else:
                print("invalid input")
        elif choice == 'B' or 'b':
            print("""
                  ***** CAR MENU *****
                  1. Display available cars
                  2. Request a car on hourly basis 
                  3. Request a car on daily basis 84 $
                  4. Return a car
                  5. Main Menu
                  6. Exit
                  """)
            try:
                choice = int(choice)
            except ValueError:
                print("its not int") 
                continue
            if choice == 1:
                
                car.display_stock()
                choice = "B"
            
            elif choice == 2:
                customer.rental_basis_c = car.rent_hourly(customer.request_vehicle("car"))
                customer.rental_basis_c = 1
                main_menu = True
                print("--------------------")
            
            elif choice == 3:
                customer.rental_basis_c = car.rent_daily(customer.request_vehicle("car"))
                customer.rental_basis_c = 2
                main_menu = True
                print("--------------------")
            
            elif choice == 4:
                customer.bill = car.return_vehicle(customer.return_vehicle("car"), "car")
                customer.rental_basis_c, customer.rental_time_c, customer.cars = 0,0,0
                main_menu = True
            
            elif choice == 5 :
                main_menu = True
           
            elif choice == 6:
                break
            
            else:
                print("invalid input")
        elif choice == "Q" or "q":
            break
        else:
            print("invalid input")
            main_menu = True
            
                
                
                
                