#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

m = 3

def Poisson():
    poisson = [0]
    while poisson[-1] <= m:
        poisson.append(poisson[-1] + np.random.exponential(1/25))
    return len(poisson) - 1


def Monte_Carlo():
    vecPois = []
    vecSpent = []
    for _ in range(10000):
        p = Poisson()
        vecPois.append(p)
        vecSpent.append(sum(np.random.uniform(5, 95, p)))
    mean, var, prob = Calc_Properties(vecPois, vecSpent)
    print("Completed 10 000 iterations. \nMean: " + str(mean) + "\nVariance: " + str(var) + "\nStandard devation: " + str(np.sqrt(var)) + "\nProbability of more than " + str(2000*m) + " being spent: " + str(prob) )


def Calc_Properties(vecPois, vecSpent):
    mean = np.mean(vecSpent)
    var = np.var(vecSpent)
    #now we calculate probability of people spending more than 2000*m 
    count = 0
    for item in vecSpent:
        if item >= 2000*m:
            count += 1
    prob = count/len(vecSpent)
    return mean, var, prob


def DrawPlot():
    y = [0]
    while y[-1] <= m:
        y.append( y[-1] + np.random.exponential(1/25))
    x = np.cumsum(np.random.uniform(5, 95, len(y)))
    plt.step(x,y, c='magenta')
    plt.xlabel('Amount Spent')
    plt.ylabel('Time')
    plt.suptitle('Compound Pоisson Process', fontsize=25)
    plt.show()


if __name__ == "__main__":
    Monte_Carlo()
    DrawPlot()
