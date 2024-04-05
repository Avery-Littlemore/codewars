# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    num_list = numbers.split(' ')
    highest = int(num_list[0])
    lowest = int(num_list[0])
    for num_str in num_list:
        num = int(num_str)
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num
    return f'{highest} {lowest}'

print(high_and_low("1 2 3 4 5"))  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
