# This function recieves a string of values and returns the highest and lowest

def high_and_low(numbers):
    # Run the int function in every element of the number string
    # in python 3 map returns a map object, so it must be converted into a list
    n = list(map(int, numbers.split(' ')))
    return '{} {}'.format(max(n), min(n))

def high_and_low(number):
    # returns a sorted list, the key makes each element a int when comparing values
    n = sorted(number.split(' '), key=int)
    return '{} {}'.format(n[-1], n[0])