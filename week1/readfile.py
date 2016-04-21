# f = open('./README.md', 'r')
#
# learning = f.read()
#
# f.close()
#
# print(learning)
# print(len(learning))

f = open('/usr/share/dict/words', 'r')
#words = f.readlines()

# We *must* close the file when we are done with it.
# try...except...finally... lets us do that!
#
# try:
#     doubleEnns = []
#     for line in f:
#         if 'nn' in line:
#             doubleEnns.append(line.strip())
# except:
#     pass #handle exception here
# finally:
#     f.close()
#

# An even better way (Python 3 only!)
doubleEnns = []

with open('/usr/share/dict/words', 'r') as f:
    try:
        for line in f:
            if 'nn' in line:
                doubleEnns.append(line.strip())
    except:
        pass #< never do this!
        


#f.close()

print(doubleEnns)

# print(len(words))
#
# print(words[50:60])

# for word in words:
#     if 'nn' in word:
#         print(word.strip())
