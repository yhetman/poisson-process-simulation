import numpy as np
import matplotlib.pyplot as plt

eps = 50
lam = 2
cycles = 20000
n = probab = appear = 0

N_t = np.arange(0, eps, 1)
plt.step(np.cumsum(np.random.exponential(1/lam, eps)), N_t, c='purple')
plt.show()

for _ in range(cycles):
    find = 3
    for i, every in enumerate(np.cumsum(np.random.exponential(1/lam, eps))):
        if every > 3:
            if N_t[i - 1] == 3 * lam:
                find -= 1
        if every > 10:
            if N_t[i - 1] == 9 * lam:
                find -= 1
        if every > 15:
            if N_t[i - 1] > 14 * lam:
                find -= 1
    if find == 0:
        probab += 1
print("Probability is " + str(probab/cycles))
for _ in range(cycles):
    for j, every in enumerate(np.cumsum(np.random.exponential(1/lam, eps))):
        if every > 10:
            n = n + N_t[j - 1]
            appear = appear + 1
            break
print("Average is " + str(n/appear))
