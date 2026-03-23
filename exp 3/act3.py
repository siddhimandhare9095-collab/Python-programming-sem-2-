# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:45:00 2026

@author: siddhi
"""
for num in range(1, 11):
    print("Table of", num)
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
    print()  # blank line after each table
