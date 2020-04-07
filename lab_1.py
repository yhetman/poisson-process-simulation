import random
import numpy as np
import matplotlib.pyplot as plt

steps = 21
lambd = 2
ksi = []
n = 0

for i in range (0,100):
    ksi = np.random.exponential(lambd, steps)
    sums = np.cumsum(ksi)
    n = n + sums[10]

arifm_mean = n/100

print("Average value of X(10) = %.6f" % (arifm_mean))
print ()


t = np.arange(0, steps, 1)
fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor = 'pink')
ax.set(facecolor = 'pink')
plt.title('Poisson Process',
        fontdict={ 'fontsize': 21},
        y=1.03, color='navy') 
ax.plot(t, sums, linestyle = 'steps-post',
        c='indigo')
plt.show()
