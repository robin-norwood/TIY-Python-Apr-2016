# Write a function that takes a string, and returns a new string with every word reversed.
#
# reverse_words("Hello, my name is Daniel") # returns ",olleH ym eman si leinaD"
#
#

def reverse_words(sentence):
    # split the string into a list by spaces
    words = sentence.split()
    # reverse each word
    #   Create an string variable
    new_words = []
    for word in words:
        new_words.append(word[::-1])
#        new_string = new_string + word[::-1] + ' '
    #   Iterate over the list
    #   Reverse the word
    #   Add the reverse word to a string

    # join into a new string
#    new_string = new_string.trim()

    return ' '.join(new_words)

#    return new_string
