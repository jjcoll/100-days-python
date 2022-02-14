#  Will find the common denomintor fraction of a list of fractions, and return a list of fractions with the same denominator

import math
def convert_fracts(lst):
    if len(lst) > 0:
        a = []
        # get all the denominators of fractions
        for i in range(len(lst)):
            a.append(lst[i][1])
        lcm = a[0]
        # find the lcm of all the denominators
        for i in range(1,len(a)):
            lcm = lcm*a[i]//math.gcd(lcm, a[i])
        answer = []
        # find the nominator
        for i in range(len(lst)):
            answer.append([ int(lcm//lst[i][1]) * lst[i][0], lcm    ])
        return answer
    else:
        return lst