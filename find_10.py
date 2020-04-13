# Yuliia Hetman, [13.04.20 22:09]

import matplotlib.pyplot as plt
import numpy as np
import math

y = np.arange(0,40,1)
x = np.cumsum(np.random.exponential(0.5,40))

print(x)
   
plt.step(x,y, c='magenta')
plt.xlabel('time')
plt.ylabel('process')
plt.suptitle('Poisson Process', fontsize=25)
plt.show()

samples = []
for _ in range(100):
    x = np.cumsum(np.random.exponential(0.5,40))
    for i, item in enumerate(x):
        if item > 10:
            samples.append(y[i-1])

mean = np.mean(samples)
print(samples)
print('Mean for t=10 is ' + str(mean))
