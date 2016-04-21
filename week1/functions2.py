
def cube_reverse(aList):
    # reverse a list, then cube each element
    newList = gimme_reversed(aList)
    newNewList = []
    for item in newList:
        newNewList.append(item ** 3)

    return newNewList

def gimme_reversed(aList):
    new = []
    for item in aList[-1::-1]:
        new.append(item)
    return new

myList = list(range(0,10))
print(myList)

newList = cube_reverse(myList)

print(newList)
