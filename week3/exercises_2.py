# Exercise 1:
#
# Write a function that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and returns a new list of only the first and last elements of the given list.

a = [5, 10, 15, 20, 25]
def  firstAndLast(inputList):
    """Return a list containing the first and last element of input"""
    return [inputList[0], inputList[-1]]

print(firstAndLast(a))


# Exercise 2:
# Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. In other words, it makes the elements of the list unique.

def unicornify(aList):
    """Return a uniquified version of aList"""
    aNewList = []
    for item in aList:
        if item not in aNewList:
            aNewList.append(item)

    return aNewList

def unic(aList):
    return list(set(aList))

names = ['Joe', 'Schmoe', 'Flo', 'Ro', 'Joe', 'Towhead', 'Flo']
# Should get back: ['Joe', 'Schmoe', 'Flo', 'Ro', 'Towhead']

print(unicornify(names))
print(unic(names))
