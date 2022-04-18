''' for commit
    git status
    git add (file_name)
    git commit -m 'master'
'''


def power(a, n):
    """"Возведение в степень"""
    f = 1
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, abs(n))

    while n != 0:
        n -= 1
        f *= a
    return f


def reduce_fraction(num, degree):
    """"Сокращение дроби"""

    for i in range(1, max(num, degree)+1):
        if num % i == 0 and degree % i == 0:
            greatest_common_divisor = i
    return num // greatest_common_divisor, degree // greatest_common_divisor


def matrix_speral(w, h):
    ''' Заполнение матрицы по спирали '''
    matrix = [[0]*h for i in range(w)]
    dx, dy, x, y = 0, 1, 0, 0

    for i in range(1, w * h + 1):
        matrix[x][y] = i
        if matrix[(x + dx) % w][(y + dy) % h]:
            dx, dy = dy, -dx
        x += dx
        y += dy    
    return matrix


class Matrix:
    ''' Класс кофигурирует или выводит уже готовую матрицу  '''
    def __init__(self, weidth, heigh) -> None:
        self.weidth = weidth
        self.heigh = heigh

    def make(self, filler):
        arr = [['']*self.heigh for i in range(self.weidth)]

        for w in range(self.weidth):
            for h in range(self.heigh):
                arr[w][h] = filler

        return self.printed(arr)
    
    def printed(self, arr):
        for w in range(len(arr)):
            for h in range(len(arr[w])):
                print(arr[w][h], end = ' ')
            print()
        return ''


def simetria(num):
    ''' Проверка на полиндром 4х значного числа '''

    num = str(num)
    if num[0] == num[-1] and num[1] == num[2]: return True
    return False


def super_polindrom(val):
    ''' Проверка на полиндром слов/предложений, исключая не буквы '''

    res = ''
    for i in range(len(val)):
        if (65 <= ord(val[i]) <= 90 or
            97 <= ord(val[i]) <= 122 or
            192 <= ord(val[i]) <= 255):
            res += val[i]
    return res.upper()==res[::-1].upper()


def eho_unix(file):
    ''' Инициализация файла с нумерацией строк '''
    line_id = 1
    with open('test.txt', encoding='utf-8', newline='') as f:
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
    ''' Разложение на простые множители '''

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
