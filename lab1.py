#1
def permute(A):
    if len(A)==1:
        return [tuple(A)]
    permutations = []
    for x in A:
        for y in permute(A-{x}):
            permutations.append((x,)+y)
    return permutations
# Використовуючи власну функцію
A={1, 2, 3}
permute_all = set(permute(A))
def output(A, permute_all):
    print("Перестановки множини {}: {}".format(A, permute_all))
    print("Кількість перестановок: ", len(permute_all))
output(A, permute_all)

#2

from itertools import permutations
# Використовуючи бібліотеку itertools
permute_all = set(permutations(A))
output(A, permute_all)

#3.1

g1={1, 3, 5}
g2={1, 2, 3, 4}
g3={1, 2, 2, 1}
perm=set(permute(g1))
output(g1, perm)
perm=set(permute(g2))
output(g2, perm)
perm=set(permute(g3))
output(g3, perm)

#3.2

G1={1, 2, 3, 4, 5}
G2={1, 2, 3, 4, 5, 6, 7}
G3={1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
perm=set(permute(G1))
print('Кількість перестановок:', len(perm))
perm=set(permute(G2))
print('Кількість перестановок:', len(perm))
perm=set(permute(G3))
print('Кількість перестановок:', len(perm))

#3.3
A=[1, 3, 4, 11, 13, 15, 16, 19, 22, 25]
B=[]
k=1
while k<=9:
    for i in range(len(A)-k):
        b=A[i+k]+A[k-1]
        B.append(b)
    k=k+1
#else 10!/(8!*2!)
print('3.3)Довжина множини B утвореної з попарних сум 10 елементної множини', len(B))
#4.1
from itertools import combinations_with_replacement
A={1, 2, 3}
k=2
def comb(A, k):
    choose_k = list(combinations_with_replacement(A,k))
    print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
    print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
comb(A, k)
#4.2
#a
n={1, 2, 3, 4}
k=2
comb(n, k)
#b
n={1, 2, 3, 4}
k=3
comb(n, k)
#c
n={1, 2, 3, 4, 5}
k=2
comb(n, k)
#d
n={1, 2, 3, 4, 5, 6}
k=2
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
#e
n={1, 2, 3, 4, 5, 6}
k=4
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
#f
n={1, 2, 3, 4, 5, 6, 7, 8}
k=4
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
#4.3
from itertools import product
p=product('1234567890', '1234567890')
p1=product('1234567890', p)
p1=list(p1)
k=0
for i in range(len(p1)):
    sum1=int(p1[i][0])+int(p1[i][1][0])+int(p1[i][1][1])
    for j in range(len(p1)):
        sum2=int(p1[j][0])+int(p1[j][1][0])+int(p1[j][1][1])
        if sum1==sum2:
            k=k+1
print('Кількість 6 цифрових наборів цифер таких що сума перших 3 дорівнює сумі останніх 3: ', k)
#4.4
from itertools import repeat
p=product('1234567890', repeat=5)
p1=product('123456789', p)
p1=list(p1)
ans=0
for i in range(len(p1)):
    m=0
    if p1[i][0]==p1[i][1][0]:
        m=1
    for j in range(4):
        if m==1:
            break
        elif p1[i][1][j]==p1[i][1][j+1]:
            m=1
            break
    if m==0:
        ans=ans+1
print('Кількість таки 6 цифрових чисел що два однакових числа не стоять поряд', ans)
