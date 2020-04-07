import random
import numpy as np
import matplotlib.pyplot as plt

eps = 21
x = [0]
y = np.arange(0, eps, 1)
ry = []
n = 0

for i in range (0,100):
    ry = []
    x = [0]

    for i in range (0,eps):
       ry.append(random.expovariate(10))

    for i in range (0,20):
       x.append(x[i]+ry[i])
    n = n + x[10]

print(n/100)
print ()

fig, ax = plt.subplots()
ax.plot(y, x, linestyle = 'steps-post')
plt.show()


        
        
