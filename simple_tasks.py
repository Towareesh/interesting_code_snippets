# for commit:
# git status
# git add (file_name)
# git commit -m 'master'
# git push


def power(a, n):
    ''' Return a^n.
    '''
    f = 1
    if n == 0: return 1
    if n < 0 : return 1 / power(a, abs(n))
    while n != 0:
        n -= 1
        f *= a
    return f


def reduce_fraction(num, degree):
    ''' Fraction reduction: (5, 40) >> (1, 8).
        Return tuple(num, degree).
    '''

    for i in range(1, max(num, degree)+1):
        if num % i == 0 and degree % i == 0:
            greatest_common_divisor = i
    return num // greatest_common_divisor, degree // greatest_common_divisor


def matrix_speral(weidth, heigh):
    ''' Filling the matrix in a spiral.
        Return a matrix with dimensions (weidth, heigh).
    '''
    matrix = [[0]*heigh for i in range(weidth)]
    dx, dy, x, y = 0, 1, 0, 0

    for i in range(1, weidth * heigh + 1):
        matrix[x][y] = i
        if matrix[(x + dx) % weidth][(y + dy) % heigh]:
            dx, dy = dy, -dx
        x += dx
        y += dy    
    return matrix


class Matrix:
    ''' Сlass return a filled matrix.
    '''
    def __init__(self, weidth, heigh, filler):
        self.weidth = weidth
        self.heigh  = heigh
        self.filler = filler

    def make(self):
        ''' Return a filled matrix.
        '''
        arr = [['']*self.heigh for i in range(self.weidth)]
        for w in range(self.weidth):
            for h in range(self.heigh):
                arr[w][h] = self.filler
        return arr
    
    def printed(self, arr):
        ''' Matrix output to the console.
            Return None.
        '''
        for w in range(len(arr)):
            for h in range(len(arr[w])):
                print(arr[w][h], end = ' ')
            print()
        return


def super_polindrom(val):
    ''' Checking for a palindrome, excluding non-letters.
    '''
    res = ''
    for i in val:
        if (65 <= ord(i) <= 90 or
            97 <= ord(i) <= 122 or
            192 <= ord(i) <= 255):
            res += i
    return res.upper()==res[::-1].upper()


def eho_unix(file):
    ''' Opening a file with line numbering.
    '''
    line_id = 1
    with open(file, encoding='utf-8', newline='') as f:
        for line in f:
            line_id += 1
            print('{0:>6} {1}'.format(line_id, line.rstrip()))
    return None


def nod(x, y):
    for i in range(max(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def fibonachi(n):
    if n == 1 or n == 0:
        return n
    return fibonachi(n-1) + fibonachi(n-2)


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def decompos_isprime(num):
    ''' Prime factorization.
    '''
    result, divisor = [], 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            result.append(divisor)
            num //= divisor
        else:
            divisor += 1
    if num > 1:
        result.append(num)
    return result


def binary_search(hash_set, item):
        midpoint = len(hash_set)//2
        if hash_set[midpoint] == item:
            return item
        else:
            if item < hash_set[midpoint]:
                return binary_search(hash_set[:midpoint], item)
            else:
                return binary_search(hash_set[midpoint + 1:], item)


def search_nums(hash_set, count_divs=4):
    ''' Search numbers the count of divisors is 'count_divs'
        Return {num: divisors}

        Results of tests:
        tests  : 20000+1 | 10000+1 | 25000+1 | 250000+1
        time_v1: 0.45s   | 0.16s   | 0.64s   | 19.44s
        time_v2: 0.33s   | 0.12s   | 0.45s   | 11.58s
        time_v2: 0.19s   | 0.08s   | 0.23s   | 6.16s

        time_v1 - version with iteration of values
        time_v2 - v1 version with a list clipper if it is full
        time_v3 - v2 version with a single call 'search_divs(i)'
    '''
    res = {}

    def search_divs(num):
        div = 1
        divisors = []
        while div ** 2 <= num:
            if num % div == 0:
                divisors.append(div)
                if div != num // div:
                    divisors.append(num // div)
            if len(divisors) > count_divs:
                return None
            div += 1
        divisors.sort()
        return divisors

    for i in hash_set:
        divisors = search_divs(i)
        if divisors != None:
            res.update({i: divisors})
    return res

print(help(search_nums))