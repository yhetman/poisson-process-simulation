import random
import numpy as np
import matplotlib.pyplot as plt

steps = 21
t = np.arange(0, steps, 1)
n = 0
lambd = 2

for i in range (0,100):
    y = []
    x = [0]

    for i in range (0,steps):
       y.append(random.expovariate(lambd))

    for i in range (0,20):
       x.append(x[i]+y[i])
    n = n + x[10]

print("Average value of X(10) =", n/100)
print ()


fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor = 'pink')
ax.set(facecolor = 'pink')
plt.title('Poisson Process',
        fontdict={'fontname': 'Times New Roman', 'fontsize': 21},
        y=1.03) 
ax.plot(t, x, linestyle = 'steps-post',
        c='magenta')
plt.show()
