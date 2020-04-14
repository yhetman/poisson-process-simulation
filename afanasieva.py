import random
import numpy as np
import matplotlib.pyplot as plt

eps = 21
t = np.arange(0, eps, 1)
n = 0
lambd = 2

for i in range (0,100):
    y = []
    x = [0]

    for i in range (0,eps):
       y.append(random.expovariate(lambd))

    for i in range (0,20):
       x.append(x[i]+y[i])
    n = n + x[10]

print("X(10) =", n/100)
plt.step(t, x, c='purple')
plt.show()


        
        