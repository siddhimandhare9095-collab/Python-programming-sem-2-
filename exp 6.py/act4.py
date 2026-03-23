# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:50:54 2026

@author: siddhi
"""
# Program: Copy data from one file to another (Backup)

source_file = "original.txt"
backup_file = "backup.txt"

# Step 1: Create source file (optional)
with open(source_file, "w") as file:
    file.write("This is original data.\n")
    file.write("Backup is important.\n")

# Step 2: Copy data to backup file
with open(source_file, "r") as src:
    data = src.read()

with open(backup_file, "w") as dest:
    dest.write(data)

print("Data copied successfully from", source_file, "to", backup_file)
