# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

def to_jaden_case(string):
    string_list = string.split()
    string_list = [substr.capitalize() for substr in string_list]
    return ' '.join(string_list)


# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

print("How can mirrors be real if our eyes aren't real")
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))