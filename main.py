# Daniel Shumeyko \\ Applied Statistics 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math


# Create a sample and plot sample path
n = 100
x = np.arange(0,20, 1/n)
y = np.cumsum(np.random.poisson(2*(1/n),20*n))

sns.set()
plt.plot(x,y, c='green')
plt.xlabel('time')
plt.ylabel('X(t)')
plt.suptitle('Pоisson Process as a Levi process', fontsize=25)
plt.show()

# Calculate mean value for t = 10 
samples = []
for _ in range(100):
    y = np.cumsum(np.random.poisson(2*(1/n),20*n))
    samples.append(y[n*10])

# Here we calculate probability that N(3)=6, N(10) = 18, N(15) > 28
occurences = 0
for _ in range(100000):
    y = np.cumsum(np.random.poisson(2*(1/n),20*n))
    if y[3*n] == 6 and y[10*n] == 18 and y[15*n] > 28:
        occurences += 1

print(samples)
print('Mean for t=10 is ' + str(np.mean(samples)))
print("The probablity of N(3)=6, N(10) = 18, N(15) > 28 is " + str(occurences/100000))
print('Program done by Daniel Shumeyko    ˙ ͜ʟ˙ ')
