 -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:47:24 2026

@author: siddhi
"""
# Program: Read and display complaints from a file

file_name = "complaints.txt"

# Step 1: Create sample complaint file (optional)
with open(file_name, "w") as file:
    file.write("Complaint Records:\n")
    file.write("1. Delay in service\n")
    file.write("2. Poor product quality\n")
    file.write("3. Late delivery\n")

# Step 2: Read and display complaints
print("List of Complaints:\n")

with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
