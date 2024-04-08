# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way 
# until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    numstr = str(n)
    while len(numstr) > 1:
        total = 0
        for char in numstr:
            total += int(char)
        numstr = str(total)
    return int(numstr)
    
        

print(digital_root(16))  #  1 + 6 = 7
print(digital_root(942))  #  9 + 4 + 2 = 15  -->  1 + 5 = 6
print(digital_root(132189))  #  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
print(digital_root(493193))  #  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
