import re


def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None



def prime_factors(n):
    limit = n
    print(limit)
    prime = [x for x in range(n) if isprime(x)]
    print(prime)
    answer = ''
    for i in prime:
        p = n
        c = 0
        while (p % i) == 0:
            p /= i
            c += 1
        if c != 0:
            if c > 1:
                answer += '({}**{})'.format(i, c)
            else:
                answer += '({})'.format(i)
    print(answer)
    return answer


prime_factors(7775460)