nested loops to print the following pattern
"""
Created on Mon Mar  9 15:27:45 2026

@author: siddhi
"""

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
   for j in range(1, i + 1):
     print(j, end=" ")
print()
