# Normal mode:
#
## Write a draw_histogram() function
# Input is a list of integers, the function prints a "histogram" based on that list.
# For draw_histogram([3, 8, 0, 2]), output is:
#
# |###
# |########
# |
# |##
# alg: 1) iterate through the list
#      2) print '|', print '#' multiplied by number, print newline.
#      3) next iteration
# Hard mode:
## Write a new draw_label_histogram() function
# Input is a dictionary, where the keys are labels, and the values are integers.
# For draw_label_histogram({'apples': 3, 'grapes': 12, 'pears': 2, 'bananas': 4})
# The output is:
#
#  apples |###
#  grapes |############
#   pears |##
# bananas |####
