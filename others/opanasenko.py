import numpy
import matplotlib.pyplot as plt

l = 8 #lambda
time = []
average = 0;
cases = 0
probability = 0.0
l = pow(l, -1)
time = numpy.arange(0, 80, 1)
for _ in range (10000):
    y = numpy.cumsum(numpy.random.exponential(l, 80))
    for i, one in enumerate(y):
        if one > 10:
            average += time[i - 1]
            cases += 1
            break
print("\nСередне значення : " + str(average/cases))
i = 0
for _ in range (10000):
    cases = 0
    y = numpy.cumsum(numpy.random.exponential(l, 80))
    for i, one in enumerate(y):
        if one > 3:
            if time[i - 1] == 3 * 8:
                cases += 1
        if one > 10:
            if time[i - 1] == 9 * 8:
                cases += 1
        if one > 15:
            if time[i - 1] > 14 * 8:
                cases += 1
    if cases == 3:
        probability += 0.0001
print("\nЙмовірність визначена за допомогою моделювання: " + str(probability))
print("\nЩо у відсотковому еквіваленті: " + str(probability*100) + "%")
fig, ax = plt.subplots()
ax.step(y, time, c = 'black')
plt.show()
