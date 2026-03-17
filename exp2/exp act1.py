# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:58:56 2026

@author: siddhi
"""
# Traffic police speed checking program

speed = float(input("Enter vehicle speed (km/h): "))

if speed > 60:
    print("Over speeding! You have to pay a fine.")
else:
    print("You are within the speed limit. Drive safely!")
