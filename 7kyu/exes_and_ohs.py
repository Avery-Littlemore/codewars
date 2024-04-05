# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.

def xo(s):
    return s.casefold().count('x') == s.casefold().count('o')

print(xo("ooxx")) # true
print(xo("xooxx")) # false
print(xo("ooxXm")) # true
print(xo("zpzpzpp")) # true // when no 'x' and 'o' is present should return true
print(xo("zzoo")) # false
