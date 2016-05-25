## Easy mode:
# Write a script that:
# Asks for the user's first name
# Asks for the user's last name
# prints out their last name, followed by a comma, then their first name.
# Ex.: first = 'Robin', last = 'Norwood', prints out "Norwood, Robin"
#

# name = {'first': '',
#         'last': ''}

import re

def valid_name_2(name):
    """Return True if the name is valid: only letters, at least len() of 2"""

    return bool(re.match(r'^\w{2,}$', name))

def valid_name(name):
    """Return True if the name is valid: only letters, at least len() of 2"""

    return len(name) >= 2 and name.isalpha()

name = {}

while not valid_name(name.get('first', '')):
    name['first'] = input("Gimme yo first name: ")

while not valid_name(name.get('last', '')):
    name['last'] = input("What your last name? ")

print("{last}, {first}".format(**name))
    # ^ equivalent of .format(first=name['first'], last=name['last'])

## Normal mode:
# Require the user to have at least two letters in each name. Keep asking until they give you two letters.

## Hard mode:
# Require that the user enter *only* letters, no numbers, symbols, or other punctuation. 'Prin$ess'
# Hint: `import re`
