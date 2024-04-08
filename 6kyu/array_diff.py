# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    result = []
    for num in a:
        if b.count(num) == 0: result.append(num)
    return result

print(array_diff([1,2],[1]) == [2])

# If a value is present in b, all of its occurrences must be removed from the other:
print(array_diff([1,2,2,2,3],[2]) == [1,3])
