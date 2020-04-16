import numpy
import matplotlib.pyplot as plt

l = 8 #lambda
time = []
average = 0
probability = 0.0
k = 100
time = numpy.arange(0, 40, pow(k,-1))
for _ in range (10000):
    X = numpy.cumsum(numpy.random.poisson(l/k, 40*k))
    average = average + X[k*10]
print("\nСередне значення : " + str(average/10000))
for _ in range (10000):
    X = numpy.cumsum(numpy.random.poisson(l/k, 40*k))
    if X[3*k] == 24:
        if X[10*k] == 72:
            if X[15*k] > 112:
                probability = probability + (1/10000)
print("\nЙмовірність визначена за допомогою моделювання: " + str(probability))
print("\nЩо у відсотковому еквіваленті: " + str(probability*100) + "%")
fig, ax = plt.subplots()
ax.step(time,X,c = 'black')
plt.show()
