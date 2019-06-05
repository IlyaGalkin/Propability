import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci

#1.1 Задана щільність

def d_f(x): # функція щільності xi
    a = 0.5
    return a * np.sin(x)

def r_f(y): # функція обернена до функції розподілу xi
    return np.arccos(1 - 2 * y)

fig, axs = plt.subplots(1,1, figsize=(20,5))
eta = sci.uniform(loc=0, scale=1)
lst_f = r_f(eta.rvs(size=10 ** 5))
axs.hist(lst_f, normed=True, bins=100)
x = np.arange(0, np.pi, 0.01)
axs.plot(x, d_f(x), color='r', lw=3)
plt.show()# демонструє графік

#1.2 Нормальний розподіл

fig, axs = plt.subplots(1,1, figsize=(20,5))
xi = sci.norm(0, 1)
eta = sci.uniform(loc=0, scale=1)
vals_eta = eta.rvs(size=100000)
vals_xi = xi.ppf(vals_eta)
axs.hist(vals_xi, normed=True, bins=100)
x = np.arange(-4, 4, 0.1)
axs.plot(x, xi.pdf(x), 'r', lw=4)
plt.show()

#2 Відсутність пам'яті

fig, axs = plt.subplots(1,2, figsize=(20,5))
xi = sci.geom(0.5)
vals = xi.rvs(size=10000)
x = np.arange(1, 11)
axs[0].hist(vals, normed=True, bins=x)
axs[0].plot(x, xi.pmf(x), 'r', lw=3)
axs[1].hist(xi.rvs(size=10000) - 1, normed=True, bins=x)
axs[1].plot(x, xi.pmf(x), 'r', lw=3)
plt.show()

#3 Задача 1.11.3

def f1(xi):
    return np.exp(-xi)

def f2(y):
    return np.ones((1, len(y)))

fig, axs = plt.subplots(1,2, figsize=(20,5))
xi = sci.expon(loc=0, scale=1)
xi_rvs = xi.rvs(size=10000)
x1 = np.arange(0, 6, 0.1)
axs[0].hist(xi_rvs, normed=True, bins=100)
axs[0].plot(x1, xi.pdf(x1), 'r', lw=3)
axs[0].set_xlim(-0.1, 6.1)
axs[1].hist(f1(xi_rvs), normed=True, bins=50, color='c')
axs[1].plot(x1, xi.pdf(x1), 'r', lw=3)
x2 = np.arange(0, 1.1, 0.1)
axs[1].plot(x2, f2(x2)[0], 'b', lw=4)
plt.show()

#3.2 Квадрат

def f3(xi):
    return xi ** 2

def f4(y):
    return np.exp(-y ** 0.5) / (2 * y ** 0.5)

fig, axs = plt.subplots(1,2, figsize=(20,5))
xi_rvs = xi.rvs(size=10000)
x1 = np.arange(0, 6, 0.1)
axs[0].hist(xi_rvs, normed=True, bins=100)
axs[0].plot(x1, xi.pdf(x1), 'r', lw=3)
axs[0].set_xlim(-0.1, 6.1)
axs[1].hist(f3(xi_rvs), normed=True, bins=np.arange(0, 3, 0.2), color='c')
x2 = np.arange(0.01, 3.01, 0.01)
axs[1].plot(x1, xi.pdf(x1), 'r', lw=3)
axs[1].plot(x2, f4(x2), 'b', lw=4)
axs[1].set_ylim(0, 2.5)
plt.show()

#5 Одиничний квадрат

xi = sci.uniform(loc=0, scale=1)
n = 100000
xi1_rvs = xi.rvs(size=n)
xi2_rvs = xi.rvs(size=n)

def f51(x, y):
    return x ** 2 + y ** 2

fig, axs = plt.subplots(1, 1, figsize=(20,5))
axs.hist(f51(xi1_rvs, xi2_rvs), normed=True, bins=150)
x2 = np.arange(0.005, 1.005, 0.01)
plt.show()

def f52(x, y):
    return np.maximum(x, y)

def d52(x):
    return 2 * x
    
fig, axs = plt.subplots(1, 1, figsize=(20,5))
axs.hist(f52(xi1_rvs, xi2_rvs), normed=True, bins=100)
x = np.arange(0, 1.02, 0.02)
axs.plot(x, d52(x), color='r', lw=4)

plt.show()

def f53(x, y):
    return abs(x - y)
    
    
def d53(x):
    return 2 * (1 - x)

 
fig, axs = plt.subplots(1, 1, figsize=(20,5))
axs.hist(f53(xi1_rvs, xi2_rvs), normed=True, bins=100)
x = np.arange(0, 1.02, 0.02)
axs.plot(x, d53(x), color='r', lw=4)

plt.show()
