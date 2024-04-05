# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

def to_camel_case(text):
    text = text.replace('-', '_')
    text = text.split('_')
    index = 1
    while index < len(text):
        text[index] = text[index].capitalize()
        index += 1
    return ''.join(text)


print(to_camel_case("the-stealth-warrior")) # "theStealthWarrior"

print(to_camel_case("The_Stealth_Warrior")) # "TheStealthWarrior"

print(to_camel_case("The_Stealth-Warrior")) # "TheStealthWarrior"