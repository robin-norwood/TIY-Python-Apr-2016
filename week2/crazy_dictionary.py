# "Easy mode"

# Write a function that:
# Takes the words from '/usr/share/dict/words'
# Sort the words in reverse order
# print the first 5
#
# https://docs.python.org/3/library/functions.html#sorted
#
#
# "Hard mode"
# Write a second function that:
# Takes the words from '/usr/share/dict/words'
#
# Remove every single-letter word from the entire list
#
# Sort the list by chopping off the first letter, and sorting by the remainder
#
# So: 'Zanzibar' comes before 'Abracadabra'
#
# prin the first 5 and last 5 from that list.

words = []
with open('/usr/share/dict/words') as f:
    for line in f:
        word = line.strip()
        if len(word) < 2:
            continue

        words.append(word)

def crazy_sorter(wd):
    return wd[1:]

words = sorted(words, key=crazy_sorter)
#print(words)

# for word in words[0:5]:
#     print(word)
# for word in words[-5:]:
#     print(word)
#
print(words)
