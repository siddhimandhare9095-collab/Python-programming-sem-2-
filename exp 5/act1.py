 -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:01:31 2026

@author: siddhi
"""

# Create dictionary
library = {
    "Python": 300,
    "Java": 400,
    "C++": 350
}

# Take input
book = input("Enter book name: ")

# Check and update price
if book in library:
    new_price = float(input("Enter new price: "))
    library[book] = new_price
    print("Price updated successfully")
else:
    print("Book not found")

# Display updated dictionary
print("Updated Library:", library)
