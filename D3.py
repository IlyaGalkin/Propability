#Dz3
#1  Задача 1.3.12
import random


def theor(n):
    if n == 3:
        return (10*9*8)/(10**3)
    elif n == 2:
        return (10*9*2)/(10**3)
    elif n == 1:
        return (10*1*1)/(10**3)
def pract(n, k):
    succ = 0
    for i in range(k):
        b=[]
        for _ in range(n):
            b.append(random.randint(1, 9))
        if len(list(set(b))) == n:
            succ += 1
    return succ/k
            

print('Theor:', theor(3))
print('Pract:', pract(3, 100000))
#ans1: 0.72
#0.69501

#2 Задача 1.3.14
import math


def pract(n, k, p, q, exp):
    nums = [i+1 for i in range(n)]
    succ = [0, 0, 0]
    for i in range(exp):
        b=[]
        for j in range(k): b.append(random.choice(nums))
        status = [1, 1, 0]
        for j in b:
            if j % p != 0:
                status[0] = 0
            if j % p != 0 and j % q != 0:
                status[1] = 0
            if j % p == 0:
                status[2] = 1
        succ[0] += status[0]
        succ[1] += status[1]
        succ[2] += status[2]
    succ[0] /= exp
    succ[1] /= exp
    succ[2] /= exp
    return succ


def theor(n, k, p, q):
    num = [i + 1 for i in range(n)]
    stats = [0, 0, 0]
    status = [1, 1, 1]
    for i in num:
        if i % p == 0:
            stats[0] += 1
            stats[2] += 1
        if i % p == 0 or i % q == 0:
            stats[1] += 1
    for j in range(k):
        if stats[0]<k: status[0] = 0
        else: status[0] = ((stats[0]/n)**k)
        if stats[1]<k: status[1] = 0
        else:  status[1] = ((stats[1]/n)**k)
        status[2] = 'Формулу считает очень долго=)'
    return status


print(pract(25, 5, 3, 4, 100000))
print(pract(25, 10, 3, 4, 100000))
print(theor(25, 5, 3, 4))
print(theor(25, 10, 3, 4))

#ans2:
#[0.00332, 0.02466, 0.85507]
#[1e-05, 0.00045, 0.97845]
#[0.0033554432000000006, 0.025480396799999996, 'Формулу считает очень долго=)']
#[0, 0.00064925062108545, 'Формулу считает очень долго=)']

#3 Задача 1.4.6

import numpy as np
import itertools

def num3(n, k):
    def check(lst):
        a, b, c = 0, 0, 0
        L = len(lst)
        for el in lst:
            l = len(el)
            l1 = len(set(el))
            if l == l1:
                a += 1
            elif l - l1 == 1:
                b += 1
            elif l - l1 == 2:
                c += 1
        return a / L, b / L, c / L

    boots = [x for x in range(1, n+1)] * 2
    # Theoretical\n",
    comb = list(itertools.combinations(boots, r=2*k))
    ev1, ev2, ev3 = check(comb)

    # Emp\n",
    N = 100000
    rand = [np.random.choice(boots, size=2*k, replace=False) for _ in range(N)]
    ev4, ev5, ev6 = check(rand)

    print('n = {}, k = {}'.format(n, k))
    print(': - отсутствует парная обувь: {:.5f};  {:.5f}\n'
          ' - ровно одна пара: {:.5f};  {:.5f}\n'
          ' - 2 пары: {:.5f};  {:.5f}\n'.format(ev1, ev4, ev2, ev5, ev3, ev6))

num3(8, 4)
num3(13, 5)

#ans3:
#n = 8, k = 4
#: - отсутствует парная обувь: 0.01989;  0.02008
# - ровно одна пара: 0.27848;  0.27799
# - 2 пары: 0.52214;  0.52207

#n = 13, k = 5
#: - отсутствует парная обувь: 0.05514;  0.05442
# - ровно одна пара: 0.31014;  0.31081
# - 2 пары: 0.43419;  0.43624


def task4(n):
    def count_sum(lst):
        s1, s2 = 0, 0
        for i in range(0, len(lst), 2):
            s2 += lst[i]
            s1 += lst[i+1]
        return s1, s2

    # при n = 25 занадто велике число для обрахунку логарифма\n",
    f = math.factorial(2 * n)
    k = np.log(f)
    prob = [np.log(x) / k for x in range(1, 2 * n + 1)]

    # theoretical probability\n",
    event1, event2 = count_sum(prob)
    print('n =', n)
    print('Theoretical probability\\n - even number: {}\\n - odd number: {}'.format(event1, event2))

    # empirical\n",
    N = 100000
    numbers = np.random.choice(list(range(1, 2 * n + 1)), size=N, replace=True, p=prob)
    event1 = len(list(filter(lambda x: x % 2 == 0, numbers))) / N
    print('Empirical probability\\n - even number: {}\\n - odd number: {}'.format(event1, 1 - event1))


task4(10)
