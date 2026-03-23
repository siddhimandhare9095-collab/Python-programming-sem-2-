# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:49:09 2026

@author: siddhi
"""
def total_stairs(n):
    # Base case
    if n == 0:
        return 0
    else:
        return 1 + total_stairs(n - 1)


# Example usage
steps = 5
print("Total stairs climbed:", total_stairs(steps))
