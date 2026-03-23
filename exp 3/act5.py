# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:13:41 2026

@author:siddhi
"""
rows = 5
cols = 6

for r in range(1, rows + 1):
    print("Row", r, end=": ")
    
    for c in range(1, cols + 1):
        print(f"S{r}{c}", end=" ")
    
    print()  # move to next row
