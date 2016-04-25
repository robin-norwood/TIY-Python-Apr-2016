#
# Roman numerals: 'cvii'
# 'i': 1
# 'v': 5
# 'x': 10
# 'l': 50
# 'c': 100
# 'm': 1000
#
# Translate a string from roman numerals to an int()
#
# Get the string from user input
# Each letter has the value described above
# Upper or lower case is fine
# Each letter value should be lower than the one before it.
# 'clxi': 161
# 'lxic': not valid
#
# Challenge mode: support 'decrements', e.g. 'iv': 4

numerals = {
'i': 1,
'v': 5,
'x': 10,
'l': 50,
'c': 100,
'm': 1000
}

total = 0
roman_num = input('Enter a Roman numeral: ')
roman_num = roman_num.lower()

# to support decrements, we need to look at the last one.
# And subtract instead of add if it's value is less than the current one.

for char in roman_num:
    total += numerals[char]

print(total)
