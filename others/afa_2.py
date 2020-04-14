import numpy as np
import matplotlib.pyplot as plt

eps = 20
lam = 1 
cycles = 200
n = probab = 0

N_t = np.arange(0, eps, pow(cycles, -1))
plt.step(np.cumsum(np.random.poisson(lam/cycles, eps*cycles)), N_t, c='purple')
plt.show()

for _ in range(cycles):
    X = np.cumsum(np.random.poisson(lam/cycles, eps*cycles))
    if X[3*cycles] == 3*lam:
        if X[10*cycles] == 9*lam:
            if X[15*cycles] > 14*lam:
                probab += 1
print("Probability is " + str(probab/cycles))
for _ in range(cycles):
    X = np.cumsum(np.random.poisson(lam/cycles, eps*cycles))
    n = n + X[10*cycles]
print("Average is " + str(n/cycles))
