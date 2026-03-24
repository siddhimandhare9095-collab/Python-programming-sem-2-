# Find common followers between two social media accounts using sets.
"""
Created on Tue Mar 24 10:29:59 2026

@author: siddhi
"""
# Followers of two accounts
account1 = {"user1", "user2", "user3", "user4"}
account2 = {"user3", "user4", "user5", "user6"}

# Find common followers
common_followers = account1.intersection(account2)

# Display result
print("Common Followers:", common_followers)
