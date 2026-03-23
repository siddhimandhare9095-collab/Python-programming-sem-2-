# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:35:11 2026

@author: siddhi
"""
# Number of receipts
receipts = 3

# Number of items in each receipt
items = 5

for r in range(1, receipts + 1):
    print("Receipt", r)
    
    for i in range(1, items + 1):
        print("Item", i)
    
    print()  # blank line after each receipt
