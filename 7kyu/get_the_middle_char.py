# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(word):
    length = len(word)
    half = int(length / 2)
    if length % 2 == 1:
        return word[half]
    else:
        return word[half - 1 : half + 1]

print(get_middle('test'))
print(get_middle('testing'))
print(get_middle('middle'))
print(get_middle('A'))