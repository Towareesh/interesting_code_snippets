# from math import pi


def my_pi(cof=15):
    count_call = 0
    res = 3 + 4/(2*3*4)

    def func(a):
        nonlocal count_call
        nonlocal res

        if count_call % 2 != 0:
            res -= 4 / a
        else:
            res += 4 / a

    for i in range(4, cof, 2):
        count_call += 1
        func(i*(i+1)*(i+2))

        prog = i/(cof//100)
        print(' {0}%'.format(prog), end='\r')

    return res


def pi_digits(n):
    "Search n digits of Pi."
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and n > 0:
            yield int(d)
            n -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


pi = [i for i in pi_digits(40000)]
print(pi[-1])