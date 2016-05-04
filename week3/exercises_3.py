# From http://www.practicepython.org/

## Exercise 1
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# nums = [1, 3, 5, 7,9]
# isInList(nums, 2) # returns False
# isInList(nums, 3) # returns True

def isInList(the_list, value):
    return value in the_list

def in_list(the_list, In):
    if In in the_list:
        return True
    else:
        return False

nums = [1, 3, 5, 7,9]
print(in_list(nums, 2)) # returns False
print(in_list(nums, 3)) # returns True


## Exercise 2
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# common_elements(a, b) # return [1, 2, 3, 5, 8, 13]
# common_elephants([1], [1, 2, 3, 4, 5]) # returns [1]
# Extras:
#
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

def common_elephants(list_a, list_b):
    new_list = []
    for i in list_a:
        if i in list_b and i not in new_list:
            new_list.append(i)

    return new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common_elephants(a, b))

def common_elements(first, second):
    return list(set(first).intersection(set(second)))
