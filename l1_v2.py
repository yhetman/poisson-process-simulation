import random
import numpy as np
import matplotlib.pyplot as plt

lambd = 8
t_10 = 0

for i in range (0,100):
    x = []
    x = np.random.exponential(lambd, 21)
    y = np.cumsum(x)
    t_10 = t_10 + y[10]

print("x(10) : ",t_10/100)

fig, ax = plt.subplots()
ax.step(np.arange(0,21,1), y, c='black')
plt.show()
