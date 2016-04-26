origStr = "List Comprehensions are the Greatest!"

vowels = 'aeiou'
newStr = ''.join([ x for x in origStr if x not in vowels ])

print(newStr)
# Lst Cmprhnsns r th Grtst!

# Use a dictionary comprehension to create a dictionary with each student's average grade:

gradebook = { 'Inara': {'Homework 1': 90,
             'Homework 2': 94,
             'Homework 3': 90 },
    'Mal':  {'Homework 1': 50,
             'Homework 2': 100,
             'Homework 3': 60},
    'Simon': {'Homework 1': 98,
              'Homework 2': 96,
              'Homework 3': 96},
    'River': {'Homework 1': 100,
              'Homework 2': 100,
              'Homework 3': 0}
              }

grade_average = { name: sum(gradebook[name].values()) / len(gradebook[name].values()) for name in gradebook }

num_grades = { name: len(gradebook[name]) for name in gradebook }
print(num_grades)
print(grade_average)

# Open /usr/share/dict/words, find every word ending in 'ace', and print a string for each: '_____ Ventura, pet detective!'

# word_file = open('...')
# ^ No problem, but we have to close the file when we're done
# word_file.close()
#
# words = word_file.readlines()


with open('/usr/share/dict/words', 'r') as word_file:
    # words = []
    # for line in word_file:
    #     word = line.strip()
    #     if word.endswith('ace'):
    #         words.append(word)

    words = [ line.strip() for line in word_file if line.strip().endswith('ace') ]

for word in words:
    pass
#    print("{0} Ventura, pet detective!".format(word.capitalize()))

# Use nested dictionary comprehensions to find the average 'Homework 3' grade from #2.

# Create a list of Water Temps for each day from the data set below.

with open('wavedata.csv') as waves_csv:
    header = waves_csv.readline().strip().split(',')
    # water_temps = []
    # for line in waves_csv:
    #     water_temps.append(line.strip().split(',')[4])

    water_temps = [ line.strip().split(',')[4] for line in waves_csv ]

print(header)
print(water_temps)

#Convert the Water Temps from Celsius to Fahrenheit as a float rounded to one decimal place

# water_temp_f = []
# for temp_c in water_temps:
#     temp_f = float(temp_c) * 1.8 + 32
#     water_temp_f.append(round(temp_f, 1))

#water_temp_f.append(round(temp_f, 1))

water_temp_f = [ round(float(temp_c) * 1.8 + 32, 1) for temp_c in water_temps ]

for temp_f in water_temp_f:
    print("{0:.1f}".format(temp_f))
#print(water_temp_f)
