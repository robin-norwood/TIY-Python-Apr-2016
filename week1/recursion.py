def add_together(first, second):
    return first + second

#print(add_together(10, 12))

# Add a series of numbers up to the given one:
# add_up(5):
# 5 + 4 + 3 + 2 + 1
# 1 + 2 + 3 + 4 + 5
# Give me the sum of all integers up to and including the given one.


def add_up(num):
    """Add a list of numbers together, return the sum."""
    aList = list(range(1, num + 1))
    sum = 0

    for item in aList:
        sum = add_together(sum, item)
#        print("NOW SUM IS: " + str(sum))

    return sum

print(add_up(10))

import traceback

def add_up_recursive(num, total=0):
    if num == 0:
        traceback.print_stack()
        print("------")
        return total
    total += num

    return add_up_recursive(num - 1, total)


print(add_up_recursive(10))


# fib series:
# 1, 1, 2, 3, 5, 8, 13,
# n = (n-2) + (n-1)

def fib(num):
    if num in (1, 2):
        return 1

    return fib(num-2) + fib(num-1)

#for i in range(1,10):
#    print(fib(i))


def fibGen():
    num1, num2 = (0, 1)

    while True:
        num1, num2 = (num2, num1 + num2)
        yield num1

f = fibGen()
print(type(f))
for x in range(10):
    print(next(f))
