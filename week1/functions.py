# if True:
#     print("Hello")
#     print("Goodbye")
#
#
# numbers = list(range(10, 200))
# print("I have", str(len(numbers)), "numbers in my list.")
#
#
# numbers = list(range(1, 21, 3))
# numbers.reverse()
# for num in numbers: print(num)


def add_together(numbers):
    sum = 0
    for n in numbers:
        sum += n

    return sum

#total = add_together(["one", "two", "three"])
#print("Tot:", total)

def greetUs(names):
    for name in names:
        print("Hello, " + name + "!")

def input_loop(prompt="Enter data: "):
    # Looks at the *arguments* to function
    # Takes each parameter
    # Assignes arguments to parameters in order
    # e.g. : prompt = arguments[0]

    inputList = []

    while True:
        userInput = input(prompt)
        if not userInput:
            break

        inputList.append(userInput)

    return inputList

# print(input_loop("Enter a city: "))
# #print(input_loop("Enter a vulcan: "))
# print(input_loop())

def other_function(param1):
    pass

def gimme_four():
    return 4

gimme_four()

def dont_gimme_four():
    pass

def concat_three(first, second, third):
    return first + second + third

#print(concat_three(1, 2, 3))

def print_three(first, second, third):
    print(first)
    print(second)
    print(third)

#print_three(2, 1, 3)

def format_color(hue, saturation, value):
    print("H: " + str(hue))
    print("S: " + str(saturation))
    print("V: " + str(value))


format_color(hue=180, saturation=.4, value=.3)


#print(concat_three(first=1, second=2, third=3))

#
# while True:
#     name = input("Name: ")
#     if not name:
#         break
#
#     nameList.append(name)
#
# greetUs(nameList)
# print(calledGreetUs)
