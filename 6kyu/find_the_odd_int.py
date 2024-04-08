# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    mydict = {}
    for num in seq:
        if mydict.get(num):
            mydict[num] += 1
        else:
            mydict[num] = 1
    for key in mydict.keys():
        if mydict[key] % 2 == 1: return key

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))