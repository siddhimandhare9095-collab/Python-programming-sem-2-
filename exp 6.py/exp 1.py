# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:33:00 2026

@author: siddhi
"""
# -*- coding: utf-8 -*-
"""
Program: File Handling in Python
Aim: To write, read, append data and count lines in a file
"""

# Step 1: Create and write to a file
file_name = "course_outcomes.txt"

with open(file_name, "w") as file:
    file.write("Course Outcomes (COs):\n")
    file.write("1. Understand the basics of Python programming.\n")
    file.write("2. Apply loops, functions, and data structures.\n")
    file.write("3. Handle files and perform basic I/O operations.\n")
    file.write("4. Solve programming problems using logic and algorithms.\n")
    file.write("5. Develop small projects using Python.\n")

print("Data written successfully.\n")

# Step 2: Read the file
print("File Content:")
with open(file_name, "r") as file:
    print(file.read())

# Step 3: Append new data
with open(file_name, "a") as file:
    file.write("6. Gain understanding of basic software development practices.\n")

print("Data appended successfully.\n")

# Step 4: Count number of course outcomes
with open(file_name, "r") as file:
    lines = file.readlines()
    outcomes = lines[1:]   # skip heading

print("Number of Course Outcomes:", len(outcomes))
