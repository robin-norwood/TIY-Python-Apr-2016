# We can validate user input to ensure expected behavior:
#
# aNumber = "default"
#
# while not aNumber.isdigit():
#     aNumber = input("Enter a number: ")
#
# aNumber = int(aNumber)
# print(5 + aNumber)

import sys

aNumber = None

while not aNumber:
    try:
        aNumber = input("Enter a number: ")
        aNumber = int(aNumber)
    except ValueError as e:
        print(type(e))
        print("Dude. No. A number. Like with digits")
        aNumber = None
    except EOFError:
        print("Fine, be that way")
        sys.exit()

print("Got a number: " + str(aNumber))
