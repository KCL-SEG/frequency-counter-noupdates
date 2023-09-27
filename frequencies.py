"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

items = ["a", "a", "b", "b", "b", "c"]

def frequencies(items):
    frequencies = {i:items.count(i) for i in items}
    # Your code goes here
    return frequencies

print(frequencies(items))
