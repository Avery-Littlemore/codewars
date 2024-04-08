# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have five or more letters reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    words = [ word if len(word) < 5 else ''.join(reversed(list(word))) for word in sentence.split() ]
    return ' '.join(words)



print(spin_words("Hey fellow warriors"))  # --> "Hey wollef sroirraw" 
print(spin_words("This is a test"))       # --> "This is a test" 
print(spin_words("This is another test")) # --> "This is rehtona test"
