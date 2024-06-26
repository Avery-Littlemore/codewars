# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without 
# any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(collection):
    if not collection:
        return []
    result = [collection[0]]
    for element in collection:
        if element != result[-1]:
            result.append(element)

    return result

print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3])
