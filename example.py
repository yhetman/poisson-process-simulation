import matplotlib.pyplot as plt
import numpy as np
import math
 
y = np.arange(0,40,1)
x = np.cumsum(np.random.exponential(0.5,40))

samples = []
occurences = 0
iters = 1000000
for _ in range(iters):
    passed = 0
    x = np.cumsum(np.random.exponential(0.5,40))
    for i, item in enumerate(x):
        if item > 3:
            if y[i-1] == 6:
                passed += 1
            if item > 10:
                if y[i-1] == 18:
                    passed += 1
            if item > 15:
                if y[i-1] > 28:
                    passed += 1
    if passed == 3:
        occurences += 1
print("The probablity of N(3)=6, N(10) = 18, N(15) > 28 is %.8f" % (occurences/iters))

plt.step(x,y, c='magenta')
plt.xlabel('time')
plt.ylabel('process')
plt.suptitle('Pоisson Process', fontsize=25)
plt.show()

