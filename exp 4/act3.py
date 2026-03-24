# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:43:46 2026

@author: siddhi
"""

feedback = input("Enter customer feedback: ")
reversed_feedback = ""

for char in feedback:
    reversed_feedback = char + reversed_feedback

print("Reversed Feedback:", reversed_feedback)
