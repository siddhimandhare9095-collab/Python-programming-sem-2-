 -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:53:36 2026

@author: siddhi
"""
# Program: Count number of words in a file

file_name = "report.txt"

# Step 1: Create sample file (optional)
with open(file_name, "w") as file:
    file.write("This is a sample report file.\n")
    file.write("It contains multiple words and lines.\n")

# Step 2: Count words
with open(file_name, "r") as file:
    content = file.read()
    words = content.split()   # split into words
    word_count = len(words)

print("Total number of words:", word_count)
