# This time no story, no theory. The examples below show you how to write function accum:

def accum(st):
    return_list = list(st)
    index = 0
    for element in return_list:
        return_list[index] = element.upper() + element.lower() * index
        index += 1

    return '-'.join(return_list)

    

print(accum("abcd")) # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty")) # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt")) # "C-Ww-Aaa-Tttt"
