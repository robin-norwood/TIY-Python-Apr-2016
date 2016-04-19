nameList = []
name = "none"
#c-style:
# char *name;
# ^ but don't quote me on that, could be wrong.

while name:
    name = input("Enter your name: ")
    if name:
        nameList.append(name)

while nameList:
    print("Hello, " + nameList.pop() + "!")

print("All done")

iters = 10
while iters:
    print("Iter number: " + str(iters))
    iters = iters - 1
