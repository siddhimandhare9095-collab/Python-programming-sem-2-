# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:47:15 2026

@author: siddhi
"""

review = input("Enter review: ")
word = input("Enter word to count: ")

words = review.lower().split()
count = words.count(word.lower())

print("The word appears", count, "times")
