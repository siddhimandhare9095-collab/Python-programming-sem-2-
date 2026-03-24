# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:23:34 2026

@author: siddhi
"""
# Inventory dictionary (item : quantity)
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

# Display current inventory
print("Current Inventory:")
for item, qty in inventory.items():
    print(item, ":", qty)

# Add new stock
item_name = input("\nEnter item name to add/update: ")
quantity = int(input("Enter quantity to add: "))

# Update inventory
if item_name in inventory:
    inventory[item_name] += quantity
else:
    inventory[item_name] = quantity

# Display updated inventory
print("\nUpdated Inventory:")
for item, qty in inventory.items():
    print(item, ":", qty)
