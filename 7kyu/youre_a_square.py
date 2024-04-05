# Given an integral number, determine if it's a square number:

from math import sqrt

def is_square(n):
    return True if n == 0 else n >= 0 and sqrt(n) % 1 == 0
    

print(is_square(-1))  #  false
print(is_square(0))  #  true
print(is_square(3))  #  false
print(is_square(4))  #  true
print(is_square(25))  #  true
print(is_square(26))  #  false