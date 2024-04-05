# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 7**2 is 49, 6**2 is 36, and 5**2 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

def square_digits(num):
    num_str = str(num)
    return_str = ''
    for char in num_str:
        return_str += str(int(char)**2)

    return int(return_str)

print(square_digits(9119))