def overlap(list1, list2):
    for item in list1:
        if item in list2:
            return True

    return False

print(overlap([1, 2, 3], [3, 2]))
print(overlap([1, 2, 3], [4, 5, 6]))

def get_overlap(list1, list2):
    overlap = []
    for item in list1:
        if item in list2:
            overlap.append(item)

    return overlap

print(get_overlap([1, 2, 3], [3, 2]))
print(get_overlap([1, 2, 3], [4, 5, 6]))


def overlap_refactor(list1, list2):
    return bool(get_overlap(list1, list2))

print(overlap_refactor([1, 2, 3], [3, 2]))
print(overlap_refactor([1, 2, 3], [4, 5, 6]))
