def concatTwo(first, second):
    return first + ' ' + second

#print(concatTwo("Joe", "BillyBob"))

def concatAll(*args):
    return ' '.join(args)

#print(concatAll())

def concatWith(sep, *strings):
    print("strings is a " + str(type(strings)))
    return sep.join(strings)

#print(concatWith(", ", "John", "George", "Ringo", "Davy"))
#print(concatWith(", "))

def printOptions(**options):
    for (k, v) in options.items():
        print('<option value="' + k + '">' + v + '</option>')

printOptions(TX="Texas", NJ="New Jersey", NC="North Carolina")


def crazyArgs(first, second, third=3, *args, **kwargs):
    print("first: " + str(first))
    print("second: " + str(second))
    print("third: " + str(third))
    for arg in args:
        print("ARG: " + str(arg))
    for (k, v) in kwargs.items():
        print("KEY: " + str(k) + ", VALUE: " + str(v))

crazyArgs(5, "second", "third", 2, 5, foo="bar", baz="bippy")
