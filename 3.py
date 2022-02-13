# for every char that is not in range a-m, that is considered an error
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"


def printer_error(s):
    not_allowed = 'nopqrstuvwxyz'
    n = 0
    d = len(s)
    for i in s:
        if i in not_allowed:
            n += 1
    return '{}/{}'.format(n,d)


# One liner 
def printer_error(s):
    # loops through s, sums the amount of char that are greater than m, this is the number of errors
    return '{}/{}'.format(sum(i > 'm' for i in s), len(s))