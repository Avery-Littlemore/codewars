# Given two integers a and b, which can be positive or negative, find the sum of all 
# the integers between and including them and return it. If the two numbers are equal return a or b.

def get_sum(a,b):
    if a > b:
        return sum(range(b, a + 1))
    else:
        return sum(range(a, b + 1))
    

print(get_sum(1, 0)) # 1 (1 + 0 = 1)
print(get_sum(1, 2)) # 3 (1 + 2 = 3)
print(get_sum(0, 1)) # 1 (0 + 1 = 1)
print(get_sum(1, 1)) # 1 (1 since both are same)
print(get_sum(-1, 0)) # -1 (-1 + 0 = -1)
print(get_sum(-1, 2)) # 2 (-1 + 0 + 1 + 2 = 2)
