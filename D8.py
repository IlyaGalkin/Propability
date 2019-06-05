import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm, uniform, beta
#1.1 Завдання 1.1
r1 = expon()
r2 = expon()
rvs1 = r1.rvs(100000)
rvs2 = r2.rvs(100000)
rvs = rvs1 / (rvs1 + rvs2)
x = np.arange(0, 1, 0.01)
plt.hist(rvs, bins=15, density=True, rwidth=0.9)
plt.plot(x, [1]*len(x), label="eta")
plt.legend()
plt.show()
#2.1 Завдання 2.1
r1 = norm()
r2 = norm()
theta = uniform(0, 2 * np.pi)
x = np.arange(-4, 4, 0.01)
rvs1 = r1.rvs(100000)
rvs2 = r2.rvs(100000)
rvs3 = theta.rvs(100000)
rvs = rvs1 * np.cos(rvs3) + rvs2 * np.sin(rvs3)
plt.hist(rvs, bins=15, rwidth=0.9, density=True)
plt.plot(x, rv1.pdf(x))
plt.show()
#2.2 Завдання
r1 = norm()
r2 = norm()
r_dzeta = lambda x: x*np.exp(-x**2/2)
x = np.arange(0, 4, 0.01)
x2 = np.arange(0, 3.1, 0.01)
rvs1 = r1.rvs(100000)
rvs2 = r2.rvs(100000)
fig, axs = plt.subplots(1, 2,figsize=[10,10])
rvs_dzeta = np.sqrt(rvs1**2 + rvs2**2)
axs[0].hist(rvs_dzeta, bins=15, rwidth=0.9, density=True)
axs[0].plot(x, r_dzeta(x))
rvs_eta = np.arccos(rvs1/rvs_dzeta)
axs[1].hist(rvs_eta, bins=10, rwidth=0.9, density=True)
axs[1].plot(x2, list(map(rv_eta,x2)))
plt.show()
#3 Рівномірний розподіл
r1 = uniform(-1,1)
r2 = uniform(-1,1)
def r3(x):
    if -2<x<0:
        return (x/2+1)/2
    elif 0<x<2:
        return (-x/2+1)/2
    else:
        return 0
rvs1 = r1.rvs(100000)
rvs2 = r2.rvs(100000)
rvs = (rvs1 + rvs2)
x = np.arange(-2, 2, 0.01)
plt.hist(rvs, bins=15, density=True, rwidth=0.9)
plt.plot(x, list(map(r3,x)))
plt.show()
