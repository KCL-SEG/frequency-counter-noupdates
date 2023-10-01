"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

items = [100, 'Hello', '100', '100', 100]






def frequencies(items):   
    itemsTwo = []

    for x in items:
        x = str(x)
        itemsTwo.append(x)

    #frequencies = {i:items.count(i) for i in items}
    frequencies = {i:itemsTwo.count(i) for i in itemsTwo}
    # Your code goes here
    return frequencies

print(frequencies(items))
