__author__ = 'Aseem'

import algos
import common
import combinatorics
import files
import lcm
import math
import numbers_ab
import primes
import series
from itertools import count, permutations


RESOURCES = 'Resources'


def prob_001():
    return series.sum_multiples_upto((3, 5), 1000)


def prob_002():
    a, b, limit = 1, 2, 4000000
    return sum(b for b in series.fibonacci(a, b, limit)
               if b % 2 == 0)


def prob_003():
    return primes.largest_prime_factor(600851475143)


def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and numbers_ab.is_palindrome(num):
                largest = num
    return largest


def prob_005():
    return lcm.lcm_of_range(1, 21)


def prob_006():
    return series.sum_numbers(100) ** 2 - series.sum_squares(100)


def prob_007():
    return primes.nth_prime(10001)


def prob_008():
    number_str = ''.join(files.get_lines(RESOURCES, '008.txt'))

    largest = 0
    consecutive = 5
    for i in range(len(number_str) - consecutive):
        product = numbers_ab.product_digits(number_str[i: i + consecutive])
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
    #TODO May be Optimized - 0.853 sec
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


def prob_018():
    return common.max_path_sum_tri_file(RESOURCES, "018.txt")


def prob_019():
    total = 0
    days = 1 + 365
    #1 for monday
    #Added 365 because 1900 isn't a leap year
    for num_days in algos.get_days(1901, 2001):
        days += num_days[1]
        days %= 7
        if days == 0:
            total += 1
    return total


def prob_020():
    return sum(int(i) for i in str(math.factorial(100)))


def prob_022():
    names = files.get_line(RESOURCES, '022.txt', split_option=',')
    names.sort()

    scores = 0
    for i in range(len(names)):
        score = 0
        for c in names[i][1:-1]:
            score += ord(c) - ord('A') + 1
        scores += (score * (i + 1))
    return scores


def prob_025():
    for b, i in zip(series.fibonacci(1, 1), count(2)):
        if len(str(b)) > 999:
            return i


def prob_029():
    return len({pow(a, b)
                for a in range(2, 101)
                for b in range(2, 101)}
               )


def prob_035():
    #TODO May be Optimized - 1.229 sec
    return(4 + sum(primes.is_circular_prime(i, len(str(i)))
                   for i in range(11, 1000000, 2)))


def prob_036():
    #TODO May be Optimized - 0.786 sec
    return sum(i for i in range(1, 1000000)
               if numbers_ab.is_palindrome(str(i)) and numbers_ab.is_palindrome(bin(i)[2:]))


def prob_040():
    s = ''
    for i in count(1):
        s += str(i)
        if len(s) >= 1000000:
            break

    total = 1
    for i in range(7):
        total *= int(s[10 ** i - 1])

    return total


def prob_041():
    largest = 0
    for i in range(1, 9):
        for j in permutations(range(1, i + 1)):
            temp = 0
            for c in j:
                temp *= 10
                temp += c
            if temp > largest and primes.is_prime(temp):
                largest = temp

    return largest


def prob_042():
    words = files.get_line(RESOURCES, "042.txt", split_option=',')
    triangles = 0
    for word in words:
        value = sum((ord(c) - ord('A') + 1)
                    for c in word[1:-1])
        if numbers_ab.is_triangle_num(value):
            triangles += 1
    return triangles


def prob_045():
    for i in count(286):
        tri_num = numbers_ab.triangle_num(i)
        if numbers_ab.is_pentagonal_num(tri_num) and numbers_ab.is_hexagonal_num(tri_num):
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
    #TODO May be Optimized - 2.348 sec
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
    import time

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        timm_t = time.time()
        print(RULER + RULER + fname + RULER + RULER)
        print(locals()[fname]())
        print("TIME " + RULER +  str(time.time() - timm_t))