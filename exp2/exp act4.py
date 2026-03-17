# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:08:32 2026

@author: siddhi
"""
# Electricity bill calculation program

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

print("Total Electricity Bill: ₹", bill)
