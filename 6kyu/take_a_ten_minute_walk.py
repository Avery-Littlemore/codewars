# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their 
# phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk 
# (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you 
# one minute to traverse one city block, so create a function that will return true if the walk the app gives you will 
# take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. 
# Return false otherwise.

def is_valid_walk(seq):
    if len(seq) != 10: return False
    x_axis = 0
    y_axis = 0
    for dir in seq:
        match dir:
            case 'n':
                y_axis += 1
            case 'e':
                x_axis += 1
            case 's':
                y_axis -= 1
            case 'w':
                x_axis -= 1

    return x_axis == 0 and y_axis == 0
