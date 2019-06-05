#Dz 2
import random

#1 Пароль

def num1():
    def get_elem():
        ls = [chr(random.randint(65, 90)), chr(random.randint(97, 122)), random.choice(num), random.choice(spec)]
        return random.choice(ls)
    key = ''
    let_up = chr(random.randint(65, 90))
    let_low = chr(random.randint(97, 122))
    num = '1234567890'
    spec = '~!@#$%^&*()-_+=\/{}[].,?<>:;'
    a1 = chr(random.randint(65, 90))
    a2 = chr(random.randint(97, 122))
    a3 = random.choice(num)
    a4 = random.choice(spec)
    key += a1+a2+a3+a4
    for i in range(6):
        key += get_elem()
    print('1 Пароль')
    print(key)
    # could be mixed once more

num1()

#ans1: Mw2>h]xHQ]

#2 Герби в ряд

def num2(n, k):
    res_list = [random.choice(['H', 'T']) for _ in range(n)]
    succ = 0
    for i in range(n - k + 1):
        ex = res_list[i:i+k]
        if 'T' not in ex:
            succ += 1
    exp_num = n - k + 1
    print('Герби в ряд')
    print("Емпіричнаична {}/{}".format(succ, n))

num2(10,2);num2(50,2);num2(100,2);
num2(10,3);num2(50,3);num2(100,3);

#ans2: Емпіричнаична 4/10
#Емпіричнаична 13/50
#Емпіричнаична 18/100
#Емпіричнаична 1/10
#Емпіричнаична 1/50
#Емпіричнаична 13/100

# Найбільше число
def num3(n, x_max, exp):
    print('n = {}, x_max = {}'.format(n, x_max))
    print('Theoretical probability: ', n*(1/6)*(x_max/6))
    succ = 0
    k1=0
    k=0
    for i in range(exp):
        for j in range(n):
            res = random.randint(1, 6)
            if res ==x_max:
                k1 = 1
            if res < x_max and k1==1:
                k = 1
            elif res > x_max :k = 0;break
        if k == 1: succ += 1;
    print('Empirical:')
    print("{}/{}".format(succ, exp))
num3(3, 6, 10)

#ans3:n = 3, x_max = 6
#Theoretical probability:  0.5

# Сума чисел
def num4(n, s, sim_num):
    succ = 0
    for i in range(sim_num):
        res_list = [random.randint(1, 6) for _ in range(n)]
        if sum(res_list) == s:
            succ += 1
    print("{}/{}".format(succ, sim_num))

num4(3, 13, 10)

#ans4:Empirical:
#6/10
#1/10
