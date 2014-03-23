__author__ = 'Aseem'

import combinatorics
import files
import lcm
import numbers
import primes
import series
from itertools import count


RESOURCES = 'Resources'


def prob_001():
    return series.sum_multiples_upto((3, 5), 1000)


def prob_002():
    a, b, limit = 1, 2, 4000000
    total = a + sum(b for b in series.fibonacci(a, b, limit)
                    if b % 2 == 0)
    return total


def prob_003():
    return primes.largest_prime_factor(600851475143)


def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and numbers.is_palindrome(num):
                largest = num
    return largest


def prob_005():
    return lcm.lcm_of_range(1, 21)


def prob_006():
    return series.sum_numbers(100) ** 2 - series.sum_squares(100)


def prob_007():
    return primes.nth_prime(10001)


def prob_008():
    number = ''
    for line in files.get_lines(RESOURCES, '008.txt'):
        number += line

    largest = 0
    for i in range(995):
        product = 1
        for j in range(5):
            product *= int(number[i + j])
        if product > largest:
            largest = product
    return largest


def prob_009():
    for c in range(1, 997):
        c_square = c * c
        for b in range(1, c):
            a = 1000 - b - c
            if a * a + b * b == c_square and b > a > 0:
                return a * b * c


def prob_010():
    #TODO May be Optimized - Level 1 of 3
    return sum(primes.primes_list(2000000))


def prob_013():
    total = sum(int(line)
                for line in files.get_lines(RESOURCES, '013.txt'))
    return str(total)[:10]


def prob_015():
    return combinatorics.combinations(40, 20)


def prob_016():
    num = str(2 ** 1000)
    return sum(int(i) for i in num)


def prob_022():
    for line in files.get_lines(RESOURCES, '022.txt'):
        names = line.split(',')
        names.sort()

        scores = 0
        for i in range(len(names)):
            score = 0
            for c in names[i][1:-1]:
                score += ord(c) - ord('A') + 1
            scores += (score * (i + 1))
        return scores


def prob_045():
    for i in count(286):
        tri_num = numbers.triangle_num(i)

        if numbers.is_pentagonal_num(tri_num) and numbers.is_hexagonal_num(tri_num):
            return tri_num


def prob_046():
    #TODO Refactor
    for i in count(9, 2):
        if primes.is_prime(i):
            continue
        for j in count(1):
            temp = i - 2 * j ** 2
            if temp < 0:
                return i
            if primes.is_prime(temp):
                break


def prob_047():
    #TODO May be Optimized - Level 1 of 3
    nums = 0
    for i in count(1):
        if primes.num_distinct_prime_factors(i) == 4:
            nums += 1
            if nums == 4:
                return i - 3
        else:
            nums = 0


def prob_048():
    return str(sum(i ** i for i in range(1, 1001)))[-10:]


if __name__ == "__main__":
    import sys

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        print(fname + RULER, end="")
        print(locals()[fname]())