# Implement a function that takes as input three arguments, and returns the largest of the three. Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!


# programming makes us dumb




# print(max_of_three(4, 7, 3)) # 7
# print(max_of_three_in_a_list([4, 7, 3])) # 7

"""
1. Look at the first one
2. Compare it to the second one
3. If the first one is greater than the second - say "first one is the bigger of the two"
4. otherwise: say "the second one is the bigger of the two"
5. take "the bigger of the two" and compare it to the next one - repeat steps 3 and 4
"""

def max_of_three(*num):
    """Takes any number of arguments, returns the biggest, or raises TypeError if two items cannot be compared."""
    heresTheBiggest = num[0]

    for n in num:
        if n > heresTheBiggest:
            heresTheBiggest = n

    return heresTheBiggest

print(max_of_three(4, 7, 3, 382, "Scotty is mean", 35, 10000)) # 7

#print(max_of_three("Larry", "Moe", "Curly")) # "Moe"

#print(max_of_three([1, 2, 3], [4, 5, 6], [4, 5, 6, 7])) # [4, 5, 6, 7]
