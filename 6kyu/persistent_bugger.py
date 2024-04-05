# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    iterations = 0
    while len(str(n)) > 1:
        product = 1
        for num in str(n):
            product *= int(num)
        n = product
        iterations += 1

    return iterations

# For example (Input --> Output):
print(persistence(39)) # 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
print(persistence(999)) # 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
print(persistence(4)) # 0 (because 4 is already a one-digit number)
