# Given two positive integers n and p, we want to find a positive integer k, if it exists, 
# such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

def dig_pow(n, p):
    numstr = str(n)
    total = 0
    for char in numstr:
        total += int(char)**p
        p += 1

    return int(total / n) if total % n == 0 else -1


n = 89
p = 1 # 1 since 8¹ + 9² = 89 = 89 * 1
print(dig_pow(n, p))

n = 92
p = 1 # -1 since there is no k such that 9¹ + 2² equals 92 * k
print(dig_pow(n, p))

n = 695
p = 2 # 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
print(dig_pow(n, p))
