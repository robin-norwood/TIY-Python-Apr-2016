# Comprehensions and generators!

myList = [1, 2, 3, 4]

#print(myList)
# return a list, doubled
def doubleMe(aList):
    newList = []
    for item in aList:
        newList.append(item * 2)

    return newList

#print(doubleMe(myList))

#doubles = [ x * 2 for x in myList ]
#print(doubles)

# When you see something like this:
#
# oldList = [ ... ]
# newLIst = []
# for item in oldList:
#     newList.append(<stuff>)
#
# You usually turn it into a comprehension like so:
# newList = [ <stuff> for x in oldList ]

#states = ["Texas", "Alabama", "North Cackalacky", "New York"]

#lcStates = [ x.lower() for x in states ]
#print(lcStates)

nums = range(1,10)
# nums = [1, 2, 3, 4, 5...9]
# ...but really a 'range' object
# def myRange(first, endBefore):
# for i in ...
#     yield i
#

#skwares = [ num ** 2 for num in nums ]
#print(skwares)

# states = {'TX': "Texas", 'NJ': "New jersey", 'MD': "Maryland"}
# def dSorter(itm):
#     return itm[0]
#
# print(sorted(states.items(), key=dSorter))

#stateNames = [states[code] for code in states]

#print(stateNames)

points = {(3, 2), (4, 5), (-8, 8), (3, -2)}

# xvalues = set()
# for pnt in points:
#     xvalues.add(pnt[0])

xvalues = {pnt[0] for pnt in points}
# Now xvalues is {3, -8, 4, 3} (or something...)

# Comprehension syntax:
# [ <expr> for <val> in <interable> ]
# { <expr> for <val> in <interable> }


#print(xvalues)
# num ** 2

# nums = range(2, 200, 4)
#
# lookupSquares = {str(num): num ** 2 for num in nums}
#
# print(lookupSquares)

# map:
# Before comprehensions, we would do it this way:

# def square(num):
#     return num ** 2
#
# print( list(map(square, range(0, 10)) ))
#
# for x in range(0,10):
#     print((lambda y: y ** 2)(x))

# x = [ x ** y for x in range(0, 10) for y in range(1, 5)]
# equivalent to:
# temp = []
#
# for x in range(0, 10):
#     for y in range(1, 5):
#         temp.append(x ** y)
#
# print(temp)

# $ pip3 install pillow
from PIL import Image

image = Image.new("RGBA", (23, 73))
image.putdata([
    (0, 224, 255, 255) if char == '1' else (0, 0, 0, 255)
    for line in open('arecibo.txt')
    for char in line.strip()
])
image.save('arecibo.png')
