 -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:00:29 2026

@author: siddhi
"""
contacts = [9876543210, 9123456780, 9876543210, 9988776655, 9123456780]

unique_contacts = []
for number in contacts:
    if number not in unique_contacts:
        unique_contacts.append(number)

print("Unique Mobile Numbers:", unique_contacts)
