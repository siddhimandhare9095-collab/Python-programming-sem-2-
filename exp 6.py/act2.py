# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:43:57 2026

@author: siddhi
"""
# Program: Student Attendance File Handling

file_name = "attendance.txt"

# Step 1: Create and write initial attendance
with open(file_name, "w") as file:
    file.write("Student Attendance Record\n")
    file.write("Name - Status\n")
    file.write("Siddhi - Present\n")
    file.write("Shreya - Absent\n")

print("Initial attendance record created.\n")

# Step 2: Append new records
with open(file_name, "a") as file:
    print("Enter new attendance records:")
    
    for i in range(2):   # add 2 new records
        name = input("Enter student name: ")
        status = input("Enter status (Present/Absent): ")
        file.write(f"{name} - {status}\n")

print("\nNew records appended successfully.\n")

# Step 3: Display file content
print("Updated Attendance Record:")
with open(file_name, "r") as file:
    print(file.read())
