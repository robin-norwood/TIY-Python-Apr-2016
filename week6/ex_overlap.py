import timeit

# Normal

## Write a function called `overlap` that takes two lists, and returns True if they have at least one item in common

#overlap([1, 2, 3], [3, 2]) # returns True
#overlap([1, 2, 3], [4, 5, 6]) # returns False

# algorithm:
# take from values of one of the lists.
# iterate through values
# compare that value to values in the next list
# if the value is found in the next list, return True
# if not, return False

# OR:
# Look at both lists, see if a value appears twice
#
# overlap([1, 2, 2, 3], [4, 5, 6])


def overlap(list1, list2):
    """Return True if an item exists in both lists, False otherwise."""
    for item in list1:
        if item in list2:
            return True
#        else:
#            return False # Does this work?

    return False

print(timeit.Timer('overlap([1, 2, 3], [2, 3])', "from __main__ import overlap").timeit())

print(overlap([1, 2, 3], [3, 2])) # returns True
print(overlap([1, 2, 3], [4, 5, 6])) # returns False


# Challenge
## write a function called `get_overlap` that takes two lists, and returns a list containing the overlapping items, or an empty list if there is no overlap

#get_overlap([1, 2, 3], [3, 2]) # returns [2, 3] (or [3, 2])
#get_overlap([1, 2, 3], [4, 5, 6]) # returns []

    # create an empty list
    # instead of return True, append to empty list

def get_overlap(list1, list2):
    """Return a list of overlapping items from list1 and list2"""
    overlap = []

    for item in list1:
        if item in list2:
            overlap.append(item)

    return overlap

print(get_overlap([1, 2, 3], [3, 2])) # returns [2, 3] (or [3, 2])
print(get_overlap([1, 2, 3], [4, 5, 6])) # returns []

def overlap_refactor(list1, list2):
    overlap = get_overlap(list1, list2)
    if len(overlap) > 0:
        return True

    return False

print(overlap_refactor([1, 2, 3], [3, 2])) # returns True
print(overlap_refactor([1, 2, 3], [4, 5, 6])) # returns False

def get_overlap_set(list1, list2):
    list(set(list1).intersection(set(list2)))

def overlap_with_set(list1, list2):
    return bool(get_overlap_set(list1, list2))

print(timeit.Timer('overlap_with_set([1, 2, 3], [2, 3])', "from __main__ import overlap_with_set").timeit())
