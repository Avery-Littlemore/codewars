# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1: return False
        
    return True

print(is_isogram("Dermatoglyphics")) # true
print(is_isogram("moose")) # false
print(is_isogram("aba")) # false
