#!/usr/bin/python
# coding:utf-8

from math import sqrt

def is_Prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

judge = True
num = 33

while judge:
    judge = False
    if not is_Prime(num):
        for i in range(1, int(sqrt(num / 2)) + 1):
            if is_Prime(num - 2 * i ** 2):
                num += 2
                judge = True
                break
    else:
        num += 2
        judge = True

print num
