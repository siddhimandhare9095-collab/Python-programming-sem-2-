# compute simple interest using a function

"""
Created on Mon Mar  9 15:38:18 2026

@author: siddhi
"""

def simple_interest(principal, rate, time):
  si = (principal * rate * time) / 100
  return si
# Taking input from the user
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
# Function call
interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)

