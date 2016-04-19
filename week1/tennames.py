# Create a List
# Prompt the user to enter 10 names
# print out the list

nameList =[]
iters = 10
while iters:
    print("ITERS: " + str(iters))
    name = input("Enter name: ")
    nameList.append(name)
    iters = iters - 1
    #if name:
    #name = input("Please enter names: ")
    #f nameList.append(name)

while nameList:
    print("Hello, "+ nameList.pop() + "!")

print("finished")
