import numpy as np
from math import sin
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, expon
param = [(0,1),(-1,1), (-2,5)]
def func(p, n=1000):
    ksi = uniform(p).rvs(n)
    sn = np.cumsum(ksi)
    s=[]
    for i in range(1, len(sn)+1):
        s+=[sn[i-1]/i]
    return s
fig, axs = plt.subplots(1, 3,figsize=[20,7])
for i in range(len(param)):
    sn = func(p[i])
    x = range(len(sn))
    axs[i].plot(x, sn)
    axs[i].plot([0,1000], [uniform(p[i]).expect(),uniform(p[i]).expect()],'r--')
    axs[i].set_title("[a,b]=[{},{}]".format(*param[i]))
m = [1,3,5,10,25,50,100]

def func1(m, n=1000):
    ek = list(norm(0,1).rvs(n))
    ck = list(uniform().rvs(m))
    ksi =[]
    for i in range(n):
        k = 0
        for k in range(m):
            k += ck[k]*ek[i-k-1]
        ksi+=[k]
    return ksi

def func2(ksi, n=1000):
    sn = np.cumsum(ksi)
    s=[]
    for i in range(1, len(sn)+1):
        s+=[sn[i-1]/i]
    return s

fig = plt.figure(figsize=[20,20])
j=0
k=0
for i in range(len(m)):
    sn = func2(func1(m[i]))
    x = range(len(sn))
    ax = fig.add_subplot(3,3,i+1)
    ax.plot(x, sn)
    ax.plot([0,1000], [m[i]-1, m[i]-1],'r--')
    ax.set_title("m={}".format(m[i]))
    j+=1
    if j==3:
        j = 0
        k += 1
plt.show()

def mk(f, n, a=0, b=1):
    z1 = []
    Q = abs(b-a)
    z = uniform(a, b).rvs(n)
    for i in z:
        if f(i):
            z1 += [i]
    if len(z) != 0:
        mA = len(z1)/len(z) * Q ** 2
    else:
        mA = 0
    return mA, z1

def mk_integral(f, mA, z1):
    S = 0
    for i in range(len(z1)):
        S += mA * f(z1[i])/len(z1)
    return S

s=[]
for n in range(1000):
    s+=[mk_integral(sin, *mk(sin,n))]
plt.plot(range(1000), s)
plt.plot([0,1000], [0.45970,0.45970], 'r--')
plt.title("sin(X) 0 to 1")
plt.show()

fig = plt.figure(figsize=[20,7])
func = lambda x: 1/x**3

ax1 = fig.add_subplot(121)
ax1.set_title("Using Exp(1)")

exp_rvs = expon(1).rvs(size=10000)
exp_rv = expon(1)

def exp_sum(ksi):
    rez =0
    for i, element in enumerate(ksi):
        rez += func(element)/exp_rv.pdf(element)
        yield rez/(i+1)


x = list(range(10000))
y = list(exp_sum(exp_rvs))
ax1.plot(x,y)
ax1.plot([1,10000],[1/2,1/2],'r--')

ax2 = fig.add_subplot(122)
ax2.set_title("Using N(0,1)")
ax2.plot(0,1)

n_rvs = norm().rvs(size=10000)
n_rv = norm()

def norm_sum(ksi):
    rez =0
    for i, element in enumerate(ksi):
        rez += func(element)/n_rv.pdf(element)*(0 if element<1 else 1)
        yield rez/(i+1)
        
x = list(range(10000))
y = list(norm_sum(n_rvs))
ax2.plot(x,y,'b')
ax2.plot([1,10000],[1/2,1/2],'r--')
plt.show()

exp_rv = expon(1)
n = (1,2,3,5,10,25,50,100,200)
mu = exp_rv.expect()
d = exp_rv.var()

def h_sum(ksi):
        rez = 0
        for i, el in enumerate(ksi):
            rez += (el-mu)
            yield rez/np.sqrt(i+1)

fig =plt.figure(figsize=[20,20])
x = np.arange(-4,4,0.01)

for i, el in enumerate(n):
    ax = fig.add_subplot(3,3,i+1)
    ax.set_title("n={}".format(el))
    hist_samples = []
    for j in range(el):
        hist_samples += list(h_sum(exp_rv.rvs(size=10000)))
    ax.hist(hist_samples, bins=20, density=True, rwidth=0.9)
    ax.plot(x, norm(0,d**2).pdf(x))
plt.show()

exp_rv = expon()
n = (1,2,3,5,10,25,50,100)
d = exp_rv.var()

def h_sum(ksi):
        rez = 0
        for i, el in enumerate(ksi):
            rez += el
            yield 2*(np.sqrt(rez)-np.sqrt(i+1))

fig =plt.figure(figsize=[20,20])
x = np.arange(-4,4,0.01)

for i, el in enumerate(n):
    ax = fig.add_subplot(3,3,i+1)
    ax.set_title("n={}".format(el))
    hist_samples = []
    for j in range(el):
        hist_samples += list(h_sum(exp_rv.rvs(size=10000)))
    ax.hist(hist_samples, bins=20, density=True, rwidth=0.9)
    ax.plot(x, norm(0,d**2).pdf(x))
plt.show()
