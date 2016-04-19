# Populate the "prisoners" dictionary with data from user input
# prisoners = { <ID>: { name: <name>, cell: <cell> }, ... }
#
# 1) Create the dictionary

prisoners = {}

ident = "default"

# while <>:
#     while <>:
#         while <>:
#             continue

while ident:
    ident = input("Enter ID: ")
    if ident == "":
        continue

    name = input("Enter Name: ")
    cell = input("Cell: ")

    prisoners[ident] = { "name": name, "cell": cell }

    print(prisoners)
