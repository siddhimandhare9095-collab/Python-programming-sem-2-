# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:40:00 2026

@author: siddhi
"""

# Program: Store daily expenses and calculate total monthly expense

file_name = "expenses.txt"

# Step 1: Write daily expenses to file
with open(file_name, "w") as file:
    print("Enter daily expenses for 5 days:")
    for i in range(1, 6):
        expense = float(input(f"Day {i} expense: "))
        file.write(str(expense) + "\n")

print("\nExpenses stored successfully.\n")

# Step 2: Read file and calculate total expense
total = 0

with open(file_name, "r") as file:
    for line in file:
        total += float(line.strip())

print("Total Monthly Expense:", total)
