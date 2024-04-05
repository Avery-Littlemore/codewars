# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    no_vowel_str = ''
    for char in string_:
        if char not in 'aeiouAEIOU':
            no_vowel_str += char
    return no_vowel_str

    # for i in "aeiouAEIOU":
    #     string_ = string_.replace(i,'')
    # return string_


print(disemvowel("This website is for losers LOL!"))