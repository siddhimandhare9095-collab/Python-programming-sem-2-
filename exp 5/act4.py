# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:26:49 2026

@author: siddhi
"""
# List of purchased items
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Dictionary to store frequency
frequency = {}

# Count frequency
for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Display result
print("Item Frequency:")
for item, count in frequency.items():
    print(item, ":", count)
